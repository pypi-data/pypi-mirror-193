from __future__ import annotations

from typing import Any, Callable, Optional

__all__ = ['read']


PROPERTIES: str = 'properties'
POINT_DEFINITION: str = 'pointDefinition'
POINTS: str = 'points'
NAME: str = 'name'
VALUE: str = 'value'
TYPE: str = 'type'

PARAMETERS: str = 'parameters'
VALUES: str = 'values'
PARAMETERS_DEFINITION: str = 'parametersDefinition'
VALUE_DEFINITIONS: str = 'valueDefinitions'
VALUES_DEFINITION: str = 'valuesDefinition'

_factory: dict[str, Callable[[str], Any]] = {
    'NUMBER': float,
    'ISO_DATE': str
}


def caps_to_camel(string: str) -> str:
    components: list[str] = string.split('_')
    return ''.join([components[0].lower()] + [item.title() for item in components[1:]])


def parse(value: str, _type: str) -> Any:
    return _factory.get(_type, str)(value)


class ValueDefinition:
    def __init__(self, data: dict[str, Any]) -> None:
        self.name: str = data[NAME]
        self.type: str = data['type']

    @classmethod
    def from_list(cls, data: list[dict[str, Any]]) -> list[ValueDefinition]:
        return [ValueDefinition(item) for item in data]


class ParameterDefinition:
    def __init__(self, data: dict[str, Any]) -> None:
        self.name: str = data[NAME]
        self.value_definitions: list[ValueDefinition] = ValueDefinition.from_list(data[VALUE_DEFINITIONS])

    @classmethod
    def from_list(cls, data: list[dict[str, Any]]) -> list[ParameterDefinition]:
        return [ParameterDefinition(item) for item in data]


class ValuesDefinition:
    def __init__(self, data: dict[str, Any]) -> None:
        self.name: str = data[NAME]
        self.type: str = data[TYPE]

    @classmethod
    def from_list(cls, data: list[dict[str, Any]]) -> list[ValuesDefinition]:
        return [ValuesDefinition(item) for item in data]


class PointDefinition:
    def __init__(self, data: dict[str, Any]) -> None:
        self.parameters_definition: list[ParameterDefinition] = ParameterDefinition.from_list(data[PARAMETERS_DEFINITION])
        self.values_definition: list[ValuesDefinition] = ValuesDefinition.from_list(data[VALUES_DEFINITION])

    def parse(self, point: dict[str, Any]) -> dict[str, Any]:
        parameters = point[PARAMETERS]
        values = point[VALUES]
        result: dict[str, Any] = {}

        for idx, parameter in enumerate(parameters):
            definition = self.parameters_definition[idx]
            for para_idx, para_item in enumerate(parameter):
                para_definition = definition.value_definitions[para_idx]
                result[caps_to_camel(para_definition.name)] = parse(para_item, para_definition.type)
        for idx, value in enumerate(values):
            if not value:
                continue
            definition = self.values_definition[idx]
            result[definition.name] = parse(value, definition.type)
            #result['value'] = parse(value, definition.type)
        return result


def read(input_data: dict[str, Any], definition: Optional[dict[str, Any]] = None) -> dict[str, Any]:
    assert PROPERTIES in input_data, f'{PROPERTIES} not in data.'

    result_obj: dict[str, Any] = {}
    for key, value in input_data.items():
        if key in (PROPERTIES, POINT_DEFINITION, POINTS):
            continue
        result_obj[key] = value
    for key, value in input_data[PROPERTIES].items():
        result_obj[caps_to_camel(key)] = value

    if definition is not None:
        assert POINTS in input_data, f'{POINTS} not in data.'
        assert VALUES_DEFINITION in definition, f'{VALUES_DEFINITION} not in data.'
        assert PARAMETERS_DEFINITION in definition, f'{PARAMETERS_DEFINITION} not in data.'

        point_definition = PointDefinition(definition)
        result_obj[POINTS] = [point_definition.parse(item) for item in input_data[POINTS]]
    else:
        if POINTS in input_data:
            raise RuntimeError(f'data has {POINTS} but no definition')

    return result_obj
