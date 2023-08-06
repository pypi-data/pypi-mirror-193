import inspect
from pathlib import Path
from typing import Any

from fire import Fire
from wheel_inspect import inspect_wheel

from ksqldb_udf.adapter import UdfHandler, UdfClass, UdfPackage, UdfParameter, function_config_param_name, \
    KsqlDbBasicTypes, KsqlDbListType, KsqlDbType, wrap_to_support_optionally_defined_parameters, KsqldbFunctionType


def _is_from_typing_module(type) -> bool:
    return hasattr(type, '__origin__')


def _get_plain_python_type(type) -> Any:
    if _is_from_typing_module(type):
        if type.__origin__ is tuple:
            return list
        return type.__origin__
    return type


_python_type_to_default_value = {
    int: -1,
    float: float('nan'),
    str: 'ERROR',
    bool: False,
    list: []
}

_basic_python_type_to_ksqldb_type = {
    int: KsqlDbBasicTypes.Long,
    float: KsqlDbBasicTypes.Double,
    str: KsqlDbBasicTypes.String,
    bool: KsqlDbBasicTypes.Boolean
}


def _python_type_to_ksqldb_type(type) -> KsqlDbType:
    if _is_from_typing_module(type):
        if type.__origin__ is list or type.__origin__ is tuple:
            item_types = set(type.__args__)
            assert len(item_types) == 1, f'Type {type} only supports a single item type. Received {item_types}'
            item_type = _basic_python_type_to_ksqldb_type[item_types.pop()]
            return KsqlDbListType(item_type)
        type = type.__origin__
    return _basic_python_type_to_ksqldb_type[type]


def build_jar_from_wheel(wheel_path: str, target_dir: str = '', group_id: str = ''):
    wheel_path = Path(wheel_path)
    assert wheel_path.exists(), f'{wheel_path} does not exist'
    target_dir = Path(target_dir) if target_dir else wheel_path.parent

    wheel_metadata = inspect_wheel(wheel_path)
    dist_info = wheel_metadata['dist_info']
    try:
        entry_points = dist_info['entry_points']['ksqldb']
    except KeyError as e:
        raise 'Wheel must define ksqldb entrypoints' from e

    package_metadata = dist_info['metadata']
    package_name = package_metadata['name']
    version = wheel_metadata['version']

    artifact_id = package_name.replace('-', '_')
    if not group_id:
        group_id = artifact_id

    extras_key = 'provides_extra'
    package_extras = '[udf]' if extras_key in package_metadata and 'udf' in package_metadata[extras_key] else ''
    udf_reqs = [f'{package_name}{package_extras}=={version}']
    classes = []
    for display_name, fn_metadata in entry_points.items():
        py_fn_name = fn_metadata["attr"]
        imported_fn_name = f'_{py_fn_name}'
        source_code = f'from {fn_metadata["module"]} import {py_fn_name} as {imported_fn_name}'
        try:
            exec(source_code)
        except ModuleNotFoundError as e:
            raise EnvironmentError(f'Failed to execute {source_code}') from e
        py_fn = eval(imported_fn_name)
        fn_signature = inspect.signature(py_fn)
        return_type = fn_signature.return_annotation
        assert return_type is not inspect.Parameter.empty, \
            f'{py_fn_name} must have a return type annotated in the form "-> type"'
        parameters = []
        for param in fn_signature.parameters.values():
            if param.name != function_config_param_name:
                assert param.annotation is not inspect.Parameter.empty, \
                    f'Parameter {param} must have a type annotated in the form "{param}: type"'
                udf_param = UdfParameter(param.name, _python_type_to_ksqldb_type(param.annotation), param.default)
                parameters.append(udf_param)

        if _is_from_typing_module(return_type) and return_type.__origin__ is list:
            ksqldb_function_type = KsqldbFunctionType.Udtf
        else:
            ksqldb_function_type = KsqldbFunctionType.Udf
        ksqldb_return_type = _python_type_to_ksqldb_type(return_type)
        # Change to always be null?
        error_value = _python_type_to_default_value[_get_plain_python_type(return_type)]
        udf_handler = UdfHandler(py_fn_name, parameters, ksqldb_return_type, error_value, ksqldb_function_type)
        wrapped_source_code = wrap_to_support_optionally_defined_parameters(source_code, py_fn_name, imported_fn_name)
        udf_class = UdfClass(display_name, wrapped_source_code, udf_reqs, [udf_handler])
        classes.append(udf_class)
    package = UdfPackage(group_id, artifact_id, version, classes, [wheel_path])
    print(package.build(target_dir))


def main():
    Fire(build_jar_from_wheel)


if __name__ == '__main__':
    main()
