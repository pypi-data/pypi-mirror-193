from __future__ import annotations

from typing import Any

from daa_utils import Log

from valuation.consts import fields, signatures
from valuation.global_settings import __type_checking__
from valuation.olympia.input.market_data_connection.source import SourceDescriptor
from valuation.engine.base_object import classproperty

if __type_checking__:
    # pylint: disable=ungrouped-imports
    from valuation.olympia.input.market_data_connection.source import Source


class Parser:
    _signature = signatures.empty
    _sources: tuple[str, ...] = ('None', )
    reference_id_pattern: str = '{ID}'
    # {ID} is means standard {reference_id} (no processing of the reference.id in this case)
    # It should be avoided even if it is redundant in order to provide more information to the user

    @classproperty
    def source_descriptors(self) -> tuple[SourceDescriptor, ...]:
        return tuple(SourceDescriptor(self._signature, _source) for _source in self._sources)

    def __init__(self, source: Source) -> None:  # pylint: disable=unused-argument
        assert source.descriptor in self.source_descriptors, f'Source {source.descriptor} not in admissible sources {self.source_descriptors}'
        self._source: Source = source

    def __str__(self) -> str:
        return f'Parser: {self._source} | Pattern: {self.reference_id_pattern}'

    def check_for(self, reference_id: str) -> bool:
        raise NotImplementedError

    def get(self, reference_id: str) -> dict[str, Any]:
        raise NotImplementedError

    def _load(self) -> None:
        raise NotImplementedError

    def _make_search_id(self, reference_id: str) -> str:
        if reference_id != reference_id.strip():
            Log.warning(f'{self} found trailing or leading spaces in {reference_id}')
        return self.reference_id_pattern.format(ID=reference_id)

    @classmethod
    def initialize_data(self) -> dict[str, Any]:
        data: dict[str, Any] = {fields.Type.key: self._signature.type}
        if self._signature.sub_type != '':
            data[fields.SubType(self._signature.type).key] = self._signature.sub_type
        return data


def get_parsers() -> dict[SourceDescriptor, type[Parser]]:
    _parsers: dict[SourceDescriptor, type[Parser]] = {}

    def _get_parsers(root: type[Parser]) -> None:
        for descriptor in root.source_descriptors:
            if descriptor.signature != signatures.empty:
                _parsers[descriptor] = root
        for child in root.__subclasses__():
            _get_parsers(child)

    _get_parsers(Parser)
    return _parsers
