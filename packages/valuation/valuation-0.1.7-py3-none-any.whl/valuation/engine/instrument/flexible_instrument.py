from __future__ import annotations

import QuantLib as ql

from valuation.consts import signatures
from valuation.consts import fields
from valuation.global_settings import __type_checking__
from valuation.engine.exceptions import QLInputError
from valuation.engine.instrument.base_object import QLInstrument
from valuation.engine.instrument.payoff_language import FinancialProgramBlock, split_financial_program
from valuation.universal_transfer import TypeKey

if __type_checking__:
    # pylint: disable=ungrouped-imports
    from valuation.engine import QLObjectDB
    from valuation.universal_transfer import DefaultParameters, Storage


class QLFlexibleInstrument(QLInstrument):                   # pylint: disable=abstract-method
    _signature = signatures.instrument.flexible_montecarlo

    def __init__(self, data: Storage, ql_db: QLObjectDB, default_parameters: DefaultParameters, data_only_mode: bool = False) -> None:
        super().__init__(data, ql_db, default_parameters, data_only_mode)

        continuous_start: ql.Date = self.data(fields.ContinuousStart, default_value=None)
        continuous_end: ql.Date = self.data(fields.ContinuousEnd, default_value=None)
        if continuous_start is None and continuous_end is None:
            self._continuous_period = None
        elif continuous_start is None or continuous_end is None:
            raise QLInputError('Both start and end need to be given or none')
        else:
            self._continuous_period = (continuous_start, continuous_end)

        pay_off_raw: list[str] = self.data(fields.PayOffDefinitions)

        if not self._documentation_mode:
            self._pay_off: str = '\n'.join(pay_off_raw)
            variables: set[str] = set()
            financial_program: FinancialProgramBlock = split_financial_program(self._pay_off)
            for line in financial_program:
                assignment_part: str = line[0][1]
                if '{' in assignment_part:
                    __, assignment_part = assignment_part[:-1].split('{', 1)
                if '|' in assignment_part:
                    assignment_parts: tuple[str, ...] = tuple(assignment_part.split('|'))
                else:
                    assignment_parts = (assignment_part, )
                for entry in line[1] + (line[0][0], ) + assignment_parts:
                    if '__' in entry:
                        variable = entry
                        if '.' in variable:
                            variable, _ = variable.split('.', 1)
                        if '[' in variable:
                            variable, _ = variable.split('[', 1)
                        variables.add(variable)

            if fields.Issue.flex in variables:
                variables.discard(fields.Issue.flex)
                self._issue__d: ql.Date = self._issue               # Simulating standard assignment to variables from above
            if fields.Maturity.flex in variables:
                variables.discard(fields.Maturity.flex)
                self._maturity__d: ql.Date = self._maturity         # Simulating standard assignment to variables from above

            for variable in variables:
                new_type_key: TypeKey = TypeKey.from_flex(variable)

                self.__setattr__(f'_{variable}', self.data(new_type_key))

            if fields.DiscountCurve.flex in variables:
                self._discount_curve = self.__getattribute__(f'_{fields.DiscountCurve.flex}')
