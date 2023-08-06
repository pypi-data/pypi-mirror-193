from __future__ import annotations

from typing import Any

from valuation.consts import signatures
from valuation.exceptions import ProgrammingError
from valuation.global_settings import __type_checking__
from valuation.engine import QLObject

if __type_checking__:
    # pylint: disable=ungrouped-imports
    from valuation.universal_transfer import Storage, Signature


class QLFactory:
    _registered_qlobjects: dict[Signature, type[QLObject]] = {}
    _virtual_objects: set[type[QLObject]] = set()

    def __init__(self, no_test: bool = True) -> None:
        self._no_test = no_test
        if self._registered_qlobjects:
            raise ProgrammingError()

    @classmethod
    def assign(cls, storage: Storage) -> type[QLObject]:
        signature = storage.signature
        return cls._registered_qlobjects[signature]

    def __enter__(self) -> None:
        class_list: list[type[QLObject]] = []

        def get_classes(root: type[QLObject]) -> None:
            if self._no_test and root.signature.type.upper().startswith('TEST'):
                return
            if root.signature != signatures.empty:  # pylint: disable=protected-access   # necessary to work with the class without instancing
                class_list.append(root)
            else:
                QLFactory._virtual_objects.add(root)
            for child in root.__subclasses__():
                get_classes(child)

        get_classes(QLObject)

        for entry in class_list:
            signature = entry.signature
            if signature in QLFactory._registered_qlobjects and QLFactory._registered_qlobjects[signature] != entry:
                raise ProgrammingError(f'Double definition of {signature}')
            QLFactory._registered_qlobjects[signature] = entry

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        QLFactory._registered_qlobjects = {}
        QLFactory._virtual_objects = set()
