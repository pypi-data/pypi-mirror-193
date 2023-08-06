from __future__ import annotations

from collections import OrderedDict, defaultdict
from dataclasses import dataclass
from typing import Optional, Union

from daa_utils.excel_io import SimpleData, StyleCollection

from valuation.consts import signatures
from valuation.consts import fields
from valuation.global_settings import __type_checking__
from valuation.olympia.input.mappings.request_keys import FIELDS
from valuation.engine.documentation import Documentation, DocumentationItem, ADDITIONAL_CHECK
from valuation.engine import QLObjectDB
from valuation.universal_transfer import NoValue, Storage, TypeKey

if __type_checking__:
    # pylint: disable=ungrouped-imports
    from valuation.engine.base_object import QLObject
    from valuation.universal_transfer import Signature
    from daa_utils.excel_io import TableData


REVERSED_FIELDS = {value: key for key, value in FIELDS.items()}

EXCEL_EXCEPTIONS: tuple[TypeKey, ...] = (
    fields.LegNumber,
    fields.QuoteCurve,
    fields.BaseCurrency,
    fields.QuoteCurrency,
    fields.FirstCouponDate,
    fields.LastCouponDate
)

for exc in EXCEL_EXCEPTIONS:
    del REVERSED_FIELDS[exc]


def has_default(item: DocumentationItem) -> bool:
    default_value = item.default_value
    return not (isinstance(default_value, NoValue) and str(default_value) == '')


@dataclass(frozen=True)
class ExcelField:
    type_key: TypeKey
    defaults: bool
    with_type: bool
    allow_fall_back: bool = False

    @property
    def key(self) -> str:
        fall_b = '(*)' if self.allow_fall_back else ''
        if self.with_type:
            field: Union[str, TypeKey] = self.type_key
        else:
            field = self.type_key.key
        return f'{field}{fall_b}'

    def __lt__(self, other: ExcelField) -> bool:
        if not self.defaults:
            if not other.defaults:
                return str(self.type_key.key) < str(other.type_key.key)
            return True
        if not other.defaults:
            return False
        return str(self.type_key.key) < str(other.type_key.key)


class ExcelFieldSubStorage:

    @property
    def key(self) -> str:
        if self._with_type:
            field: Union[str, TypeKey] = self._type_key
        else:
            field = self._type_key.key
        if not self.sub_storage_types:
            return str(field)  # should never happen
        sub_types = ', '.join(sorted(self.sub_storage_types))
        return f'{field}({sub_types})'

    @property
    def defaults(self) -> bool:
        return self._defaults

    def __init__(self, type_key: TypeKey, defaults: bool, with_type: bool) -> None:
        self._type_key = type_key
        self._defaults = defaults
        self._with_type = with_type
        self.sub_storage_types: set[str] = set()

    def add_sub_type(self, sub_storage_type: str) -> None:
        self.sub_storage_types.add(sub_storage_type)

    def __lt__(self, other: ExcelFieldSubStorage) -> bool:
        if not self.defaults:
            if not other.defaults:
                return str(self._type_key.key) < str(other._type_key.key)
            return True
        if not other.defaults:
            return False
        return str(self._type_key.key) < str(other._type_key.key)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, ExcelFieldSubStorage):
            return NotImplemented
        return self._type_key == other._type_key


class QLObjectDocumentationExcel:

    @property
    def signature(self) -> Signature:
        return self._signature

    @property
    def data_standard(self) -> list[ExcelField]:
        return self._data_standard

    @property
    def data_leg(self) -> Optional[dict[ExcelField, dict[Signature, list[ExcelField]]]]:
        if data := self._data_leg:
            return data
        return None

    @property
    def data_schedule(self) -> Optional[list[ExcelFieldSubStorage]]:
        if data := self._data_schedule:
            return data
        return None

    @property
    def types_schedule(self) -> list[tuple[str, str]]:
        return self._types_schedule

    @property
    def data_sub_storage(self) -> Optional[list[ExcelFieldSubStorage]]:
        if data := self._data_sub_storage:
            return data
        return None

    @property
    def types_sub_storage(self) -> list[tuple[str, str]]:
        return self._types_sub_storage

    def __init__(self, ql_object: type[QLObject], with_types: bool) -> None:
        self._signature: Signature = ql_object.signature
        self._data_standard: list[ExcelField] = []
        self._data_leg: dict[ExcelField, dict[Signature, list[ExcelField]]] = defaultdict(dict)
        self._data_schedule: list[ExcelFieldSubStorage] = []
        self._types_schedule: list[tuple[str, str]] = []
        self._data_sub_storage: list[ExcelFieldSubStorage] = []
        self._types_sub_storage: list[tuple[str, str]] = []
        self._with_types = with_types
        self._initialize(ql_object)

    def _initialize(self, ql_object: type[QLObject]) -> None:
        ql_object_documentation = ql_object(Storage(), QLObjectDB(), None).document
        self._data_standard = self._get_items_standard(ql_object_documentation, self._with_types)
        for type_key, multi_line_item in ql_object_documentation.data_multi_line.items():
            for signature, sub_data_standard in multi_line_item.items():
                if fields.Schedule('').key in type_key.key or type_key == fields.CallSchedule:
                    if signature.type == 'General' and self._signature != signatures.instrument.vanilla_swap:
                        continue
                    self._get_items_sub_storage(self._data_schedule, self._types_schedule, sub_data_standard, type_key, signature)
                elif fields.Legs.key in type_key.key:
                    self._data_leg[ExcelField(type_key, False, self._with_types)][signature] = self._get_items_standard(sub_data_standard, self._with_types, check_fall_back=True)
                elif fields.Schedule('').key in type_key.key:
                    continue
                else:
                    self._get_items_sub_storage(self._data_sub_storage, self._types_sub_storage, sub_data_standard, type_key, signature)

    @staticmethod
    def _get_items_standard(documentation: Documentation, with_types: bool, check_fall_back: bool = False) -> list[ExcelField]:
        items: list[ExcelField] = []
        for type_key, documentation_item in documentation.items():
            if type_key in (fields.Type, fields.SubType(''), fields.Id, fields.LegNumber):
                continue
            if type_key.type == ADDITIONAL_CHECK:
                continue
            if type_key in REVERSED_FIELDS:
                type_key = TypeKey(type_key.type, REVERSED_FIELDS[type_key])
            items.append(ExcelField(type_key, has_default(documentation_item), with_types, allow_fall_back=(check_fall_back and documentation_item.fall_back_allowed)))
        return items

    def _get_items_sub_storage(self, data2update: list[ExcelFieldSubStorage], types2update: list[tuple[str, str]], documentation: Documentation, sub_storage_type: TypeKey, sub_storage_signature: Signature) -> None:
        types2update.append((sub_storage_type.key, sub_storage_signature.type))
        for type_key, documentation_item in documentation.items():
            if type_key in (fields.Type, fields.SubType('')):
                continue
            if type_key.type == ADDITIONAL_CHECK:
                continue
            if type_key in REVERSED_FIELDS:
                type_key = TypeKey(type_key.type, REVERSED_FIELDS[type_key])
            new_item = ExcelFieldSubStorage(type_key, has_default(documentation_item), self._with_types)
            sub_type = sub_storage_signature.type if not documentation_item.fall_back_allowed else f'{sub_storage_signature.type}*'
            if new_item in data2update:
                old_item = data2update.pop(data2update.index(new_item))
                old_item.add_sub_type(sub_type)
                data2update.append(old_item)
            else:
                new_item.add_sub_type(sub_type)
                data2update.append(new_item)


def get_objects(root: type[QLObject], exceptions: Optional[list[Signature]] = None) -> list[type[QLObject]]:
    class_list: list[type[QLObject]] = []

    def get_classes(base_object: type[QLObject]) -> None:
        if base_object.signature.type.upper().startswith('TEST'):
            return
        if base_object.signature != signatures.empty and (
            not exceptions or base_object.signature not in exceptions
        ):
            class_list.append(base_object)
        for child in base_object.__subclasses__():
            get_classes(child)
    get_classes(root)
    return class_list


def set_field_style(table_data: Union[TableData, SimpleData], header: str, required: bool) -> Union[TableData, SimpleData]:
    if required:
        if isinstance(table_data, SimpleData):  # TODO(2021/10) hack of own package, add this to ExcelIO SimpleData
            table_data._data.set_single_header_style(header, border=StyleCollection.Border.Thin, alignment=StyleCollection.Alignment.Center, fill=StyleCollection.Color.Yellow)  # pylint: disable=protected-access
        else:
            table_data.set_single_header_style(header, border=StyleCollection.Border.Thin, alignment=StyleCollection.Alignment.Center, fill=StyleCollection.Color.Yellow)
    elif isinstance(table_data, SimpleData):
        table_data._data.set_single_header_style(header, border=StyleCollection.Border.Thin, alignment=StyleCollection.Alignment.Center)  # pylint: disable=protected-access
    else:
        table_data.set_single_header_style(header, border=StyleCollection.Border.Thin, alignment=StyleCollection.Alignment.Center)
    return table_data


def data_standard2table(table_data: Union[TableData, SimpleData], data_standard: Union[list[ExcelField], list[ExcelFieldSubStorage]]) -> Union[TableData, SimpleData]:
    data_no_values: dict[str, None] = OrderedDict()
    for field in sorted(data_standard):
        data_no_values[field.key] = None
    if isinstance(table_data, SimpleData):
        table_data.append(data_no_values)
    else:
        table_data.add_data_line(data_no_values)
    for field in data_standard:
        if not field.defaults:
            set_field_style(table_data, field.key, True)
        else:
            set_field_style(table_data, field.key, False)
    return table_data
