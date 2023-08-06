from abc import ABC as ABSTRACT_BASE_CLASS
from copy import deepcopy
from dataclasses import dataclass
from enum import Enum, auto
from inspect import Parameter
from math import isnan
from pathlib import Path
from shutil import rmtree as delete_dir
from string import Template
from typing import List, Any, ClassVar, Union

from ksqldb_udf import run_command


class KsqldbFunctionType(Enum):
    Udf = auto()
    Udtf = auto()


class KotlinType(Enum):
    Byte = auto()
    Short = auto()
    Int = auto()
    Long = auto()
    Float = auto()
    Double = auto()
    Boolean = auto()
    Char = auto()
    String = auto()
    BigDecimal = auto()
    ByteBuffer = auto()
    Time = auto()
    Date = auto()
    Timestamp = auto()


_ksql_supported_types = [(type.name, type.value) for type in
                         (KotlinType.Int, KotlinType.Long, KotlinType.Double, KotlinType.String, KotlinType.Boolean,
                          KotlinType.BigDecimal, KotlinType.ByteBuffer, KotlinType.Time, KotlinType.Date,
                          KotlinType.Timestamp)]
KsqlDbBasicTypes = Enum('KsqldbUdfTypes',
                        _ksql_supported_types)

unimplemented_basic_types = {KsqlDbBasicTypes.Int, KsqlDbBasicTypes.BigDecimal, KsqlDbBasicTypes.ByteBuffer,
                             KsqlDbBasicTypes.Time, KsqlDbBasicTypes.Date, KsqlDbBasicTypes.Timestamp}


class KsqlDbListType:
    def __init__(self, item_type: KsqlDbBasicTypes):
        self.item_type = item_type
        self.name = f'List<{self.item_type.name}>'


KsqlDbType = Union[KsqlDbBasicTypes, KsqlDbListType]
supported_complex_types = {KsqlDbListType}

kotlin_type_to_sql_type = {kotlin_type: kotlin_type.name for kotlin_type in
                           (KsqlDbBasicTypes.Int, KsqlDbBasicTypes.Double, KsqlDbBasicTypes.Boolean,
                            KsqlDbBasicTypes.String, KsqlDbBasicTypes.Time, KsqlDbBasicTypes.Date,
                            KsqlDbBasicTypes.Timestamp)}
kotlin_type_to_sql_type[KsqlDbBasicTypes.Long] = 'BIGINT'
kotlin_type_to_sql_type[KsqlDbBasicTypes.BigDecimal] = 'DECIMAL'
kotlin_type_to_sql_type[KsqlDbBasicTypes.ByteBuffer] = 'BYTES'
kotlin_type_to_sql_type[KsqlDbListType] = 'ARRAY'


def _encode_as_basic_kotlin_variable(value: Any) -> str:
    if isinstance(value, str):
        return f'"{value}"'
    if isinstance(value, bool):
        return str(value).lower()
    if isinstance(value, float) and isnan(value):
        return "Double.NaN"
    return value


def is_type_supported(type: KsqlDbType) -> bool:
    return type not in unimplemented_basic_types and \
           (isinstance(type, KsqlDbBasicTypes) or type.__class__ in supported_complex_types)


@dataclass
class UdfParameter:
    name: str
    type: KsqlDbType
    default_value: Any = Parameter.empty

    def __post_init__(self):
        if not is_type_supported(self.type):
            raise NotImplementedError(self.type)
        if self.default_value is not Parameter.empty and self.type == KsqlDbBasicTypes.String:
            self.default_value = f'"{self.default_value}"'

    def __repr__(self):
        return f'@UdfParameter(value="{self.name}") {self.name}: {self.type.name}?'

    __str__ = __repr__


@dataclass
class UdfHandler(ABSTRACT_BASE_CLASS):
    py_fn_name: str
    params: List[UdfParameter]
    return_type: KsqlDbType
    error_value: Any
    function_type: KsqldbFunctionType = KsqldbFunctionType.Udf
    description: str = ''
    schema: str = ''
    schema_provider: str = ''

    def __post_init__(self):
        if not is_type_supported(self.return_type):
            raise NotImplementedError(self.return_type)
        if isinstance(self.return_type, KsqlDbListType):
            list_contents = [_encode_as_basic_kotlin_variable(value)
                             for value in self.error_value]
            encoded_contents = str(list_contents)[1:-1].replace("\'", '')
            self.error_value = f'listOf({encoded_contents})'
            print(self.error_value)
        else:
            self.error_value = _encode_as_basic_kotlin_variable(self.error_value)

    def __str__(self):
        template = Template("""
    @${function_type}(description="$description")
    fun handle($udf_params): $return_type {
        logger.info("Executing $python_fn_name")
        var out: $return_type = $error_value
        try {
            pythonInstance.use { interpreter ->
                interpreter.exec($code_var_name)
                val udfFn: PyObject = interpreter.get("$python_fn_name") as PyObject
                out = udfFn.invokeMethod("__call__", functionConfigs, $udf_args) as $return_type
            }
        } catch (e: PythonEnvironmentException) {
            e.printStackTrace()
        }
        return out
    }
    """)
        param_str = ', '.join(str(param) for param in self.params)
        arg_str = ', '.join([param.name for param in self.params])
        return template.substitute(description=self.description,
                                   udf_params=param_str,
                                   python_fn_name=self.py_fn_name,
                                   return_type=self.return_type.name,
                                   udf_args=arg_str,
                                   error_value=self.error_value,
                                   function_type=self.function_type.name,
                                   code_var_name=UdfClass.code_var_name)


@dataclass
class UdfClass:
    display_name: str
    udf_code: str
    python_requirements: List[str]
    udf_handlers: List[UdfHandler]
    description: str = ""
    author: str = ""
    version: str = ""

    code_var_name: ClassVar[str] = 'udfCode'

    @staticmethod
    def _encode_python_code(code: str):
        return code.encode('unicode_escape').decode('utf-8').replace('"', r'\"')

    def __post_init__(self):
        self.udf_code = self._encode_python_code(self.udf_code)
        self.python_requirements = deepcopy(self.python_requirements)
        self.python_requirements.append('pemja==0.2.*')

        # The UDF library does not support Kotlin's default argument syntax to register multiple variants at the handler
        # level. Therefore, multiple handlers with varying parameters need generated at the class level, like for Java
        handlers = deepcopy(self.udf_handlers)
        for handler in handlers:
            for i, param in enumerate(reversed(handler.params)):
                if param.default_value is Parameter.empty:
                    break
                variant_handler = deepcopy(handler)
                variant_handler.params = handler.params[:-(i + 1)]
                self.udf_handlers.append(variant_handler)

    def build(self, package_name: str, out_dir: Path):
        udf_kotlin_code = f'package {package_name}\n{str(self)}'
        (out_dir / f'{self.display_name}.kt').write_text(udf_kotlin_code)

    def __str__(self):
        template = Template("""
import io.confluent.csid.ksqldb.udf.PythonUdf
import io.confluent.csid.python.environment.PythonEnvironmentException
import io.confluent.ksql.function.${function_type_lower}.${function_type}
import io.confluent.ksql.function.${function_type_lower}.${function_type}Description
import io.confluent.ksql.function.udf.UdfParameter
import pemja.core.`object`.PyObject


@${function_type}Description(name="$display_name", description="$udf_description")
class $display_name : PythonUdf(pythonRequirements, "$display_name") {
    companion object {
        private const val $code_var_name = "$udf_code"
        private val pythonRequirements = arrayOf($python_requirements)
    }

    $udf_handlers
}
""")
        python_requirements = '", "'.join(self.python_requirements)
        python_requirements = f'"{python_requirements}"'
        udf_handlers = '\n'.join(str(handler) for handler in self.udf_handlers)
        function_type = self.udf_handlers[0].function_type.name
        return template.substitute(
            display_name=self.display_name,
            udf_description=self.description,
            code_var_name=self.code_var_name,
            udf_code=self.udf_code,
            python_requirements=python_requirements,
            udf_handlers=udf_handlers,
            function_type=function_type,
            function_type_lower=function_type.lower()
        )


_project_dir = Path(__file__).parent
_mvn_path = _project_dir / 'mvnw'
assert _mvn_path.exists()


class UdfKotlinLib:
    def __init__(self):
        self._group_id = 'io.confluent.csid'
        self._artifact_id = 'ksqldb-udf'
        self._version = '0.1.0-SNAPSHOT'

    def install(self, install_dir: Path):
        local_maven_repo_name = "local-maven-repo"
        jar_glob_pattern = 'ksqldb-udf-python-core-[0-9].[0-9].[0-9]*-jar-with-dependencies.jar'
        kotlin_udf_lib_jar = next(_project_dir.glob(jar_glob_pattern))
        run_command(str(_mvn_path),
                    'deploy:deploy-file',
                    f'-DgroupId={self._group_id}',
                    f'-DartifactId={self._artifact_id}',
                    f'-Dversion={self._version}',
                    f'-Durl=file:{str(install_dir / local_maven_repo_name)}',
                    f'-DrepositoryId={local_maven_repo_name}',
                    '-DupdateReleaseInfo=true',
                    f'-Dfile={str(kotlin_udf_lib_jar)}')


class UdfPackage:
    def __init__(self, group_id: str, artifact_id: str, version: str, udf_classes: Union[UdfClass, List[UdfClass]],
                 local_dependencies: List[Path] = []):
        self._group_id = group_id
        self._artifact_id = artifact_id
        self._version = version
        self._udf_classes = [udf_classes] if isinstance(udf_classes, UdfClass) else udf_classes
        self._local_dependencies = local_dependencies

        self._package_dir = Path(__file__).parent
        self._build_dir = self._package_dir.parent / 'build'

    def build(self, target_dir: Path = None) -> Path:
        self._build_dir.mkdir(parents=True, exist_ok=True)
        try:
            pom_template = Template((self._package_dir / 'pom-template.xml').read_text())
            pom = pom_template.substitute(group_id=self._group_id,
                                          artifact_id=self._artifact_id,
                                          package_version=self._version,
                                          ksqldb_udf_lib_version='0.1.0-SNAPSHOT')
            (self._build_dir / 'pom.xml').write_text(pom)

            kotlin_project_dir = self._build_dir / 'src/main'
            code_dir = kotlin_project_dir / 'kotlin'
            code_dir.mkdir(parents=True, exist_ok=True)
            for udf_class in self._udf_classes:
                udf_class.build(self._group_id, code_dir)
            if self._local_dependencies:
                wheel_dir = kotlin_project_dir / 'resources' / 'python-dependencies'
                wheel_dir.mkdir(parents=True, exist_ok=True)
                for local_dependency in self._local_dependencies:
                    wheel_dir.joinpath(local_dependency.name).write_bytes(local_dependency.read_bytes())

            UdfKotlinLib().install(self._build_dir)
            run_command(str(_mvn_path), 'clean', 'package', '-f', str(self._build_dir))
            udf_jar_path = self._build_dir / f'target/{self._artifact_id}-{self._version}.jar'
            assert udf_jar_path.exists()
            if target_dir is None:
                target_dir = Path().cwd()
            target_dir.mkdir(parents=True, exist_ok=True)
            output_path = target_dir / udf_jar_path.name
            udf_jar_path.rename(output_path)
        finally:
            delete_dir(self._build_dir)
        return output_path


function_config_param_name = 'function_configs'


def wrap_to_support_optionally_defined_parameters(code: str, fn_name: str, inner_fn_name: str) -> str:
    return f"""
{code}
def {fn_name}({function_config_param_name}, *args):
    kwargs = dict()
    if '{function_config_param_name}' in {inner_fn_name}.__code__.co_varnames:
        print('{function_config_param_name} found in function')
        kwargs['{function_config_param_name}'] = {function_config_param_name}
    else:
        print('{function_config_param_name} NOT found in function')
    print('Calling {fn_name}')
    try:
        return {inner_fn_name}(*args, **kwargs)
    except BaseException as e:
        print(e)"""
