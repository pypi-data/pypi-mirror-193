from __future__ import annotations

import inspect
import math
import operator
import re
from collections import defaultdict
from functools import reduce
from typing import Any, Callable, Iterable, Optional, Tuple, Union

import QuantLib as ql
from scipy.stats import norm

from valuation.consts import pl
from valuation.exceptions import ProgrammingError
from valuation.global_settings import __type_checking__
from valuation.engine.market_data import QLYieldCurve
from valuation.engine.utils import CashFlowDescriptor
from valuation.universal_transfer import Reference
from valuation.utils.decorators import memoize
from valuation.utils.other import de_listify, listify, zip_listify

if __type_checking__:
    # pylint: disable=ungrouped-imports
    from valuation.engine.instrument import QLInstrument
    from valuation.engine.instrument.coupons.base_object import QLCoupon
    from valuation.engine.process.path import Path


StackValue = Union[float, list[float]]
Stack = list[StackValue]


def local_import_cdf(value: float) -> float:
    return norm.cdf(value)          # type: ignore[no-any-return]


class Operator:
    @property
    def precedence(self) -> Union[int, float]:
        return self._precedence

    def __init__(self, precedence: Union[int, float]):
        self._precedence: Union[int, float] = precedence

    def __call__(self, stack: Stack, variables: dict[str, StackValue], path: Path, observation: Optional[int], tolerance_for_equality: Optional[float] = None) -> None:
        raise NotImplementedError


class CalcOperator(Operator):       # pylint: disable=abstract-method
    def __init__(self, precedence: int, local_operator: Callable[..., float], name: Optional[str] = None) -> None:
        super().__init__(precedence)
        self._local_operator: Callable[..., float] = local_operator
        self._name = name or self._local_operator.__name__

    def __str__(self) -> str:
        return self._name


class BinaryOperator(CalcOperator):
    def __call__(self, stack: Stack, variables: dict[str, StackValue], path: Path, observation: Optional[int], tolerance_for_equality: Optional[float] = None) -> None:
        value_right: StackValue = stack.pop(-1)
        value_left: StackValue = stack.pop(-1)
        value: list[float] = [self._local_operator(v_left, v_right) for v_left, v_right in zip_listify(value_left, value_right)]
        stack.append(de_listify(value))


class ComparisonOperator(BinaryOperator):
    def __call__(self, stack: Stack, variables: dict[str, StackValue], path: Path, observation: Optional[int], tolerance_for_equality: Optional[float] = None) -> None:
        value_right: StackValue = stack.pop(-1)
        value_left: StackValue = stack.pop(-1)
        value: list[float] = [self._local_operator(v_left, v_right, tolerance_for_equality) for v_left, v_right in zip_listify(value_left, value_right)]
        stack.append(de_listify(value))


class UnaryOperator(CalcOperator):
    def __call__(self, stack: Stack, variables: dict[str, StackValue], path: Path, observation: Optional[int], tolerance_for_equality: Optional[float] = None) -> None:
        stack_value = stack.pop(-1)
        value: list[float] = [self._local_operator(s_value) for s_value in listify(stack_value)]
        stack.append(de_listify(value))


class CombinationOperator(UnaryOperator):
    def __call__(self, stack: Stack, variables: dict[str, StackValue], path: Path, observation: Optional[int], tolerance_for_equality: Optional[float] = None) -> None:
        stack_value: StackValue = stack.pop(-1)
        stack.append(reduce(self._local_operator, listify(stack_value)))


class AppendOperator(Operator):     # pylint: disable=abstract-method
    def __init__(self) -> None:
        super().__init__(float('nan'))


class AppendValue(AppendOperator):
    def __init__(self, value: StackValue) -> None:
        super().__init__()
        self._value = value

    def __call__(self, stack: Stack, variables: dict[str, StackValue], path: Path, observation: Optional[int], tolerance_for_equality: Optional[float] = None) -> None:
        stack.append(self._value)

    def __str__(self) -> str:
        return str(self._value)


class AppendVariable(AppendOperator):
    def __init__(self, variable_name: str) -> None:
        super().__init__()
        self._variable_name: str = variable_name

    def __call__(self, stack: Stack, variables: dict[str, StackValue], path: Path, observation: Optional[int], tolerance_for_equality: Optional[float] = None) -> None:
        stack.append(variables[self._variable_name])

    def __str__(self) -> str:
        return self._variable_name


class AppendUnderlying(AppendOperator):
    def __init__(self, underlying_name: str) -> None:
        super().__init__()
        self._underlying_name: str = underlying_name

    def __call__(self, stack: Stack, variables: dict[str, StackValue], path: Path, observation: Optional[int], tolerance_for_equality: Optional[float] = None) -> None:
        if observation is None:
            raise ProgrammingError()
        value = path.value(observation, self._underlying_name)
        stack.append(value)

    def __str__(self) -> str:
        return f'PATH[{self._underlying_name}]'


class LeftBracket(Operator):    # pylint: disable=abstract-method
    def __init__(self) -> None:
        super().__init__(float('-inf'))

    def __str__(self) -> str:
        return '('


class RightBracket(Operator):   # pylint: disable=abstract-method
    def __init__(self) -> None:
        super().__init__(float('nan'))

    def __str__(self) -> str:
        return ')'


class Separator(Operator):
    def __init__(self) -> None:
        super().__init__(float('-inf'))

    def __str__(self) -> str:
        return ','

    def __call__(self, stack: Stack, variables: dict[str, StackValue], path: Path, observation: Optional[int], tolerance_for_equality: Optional[float] = None) -> None:
        value_right: StackValue = stack.pop(-1)
        value_left: StackValue = stack.pop(-1)
        value: list[float] = listify(value_left) + listify(value_right)
        stack.append(value)


def bigger(value_left: float, value_right: float) -> float:
    return 1 if value_left > value_right else 0


def bigger_equal(value_left: float, value_right: float) -> float:
    return 1 if value_left >= value_right else 0


def smaller(value_left: float, value_right: float) -> float:
    return 1 if value_left < value_right else 0


def smaller_equal(value_left: float, value_right: float) -> float:
    return 1 if value_left <= value_right else 0


def bigger_tolerance(value_left: float, value_right: float, tolerance_for_equality: Optional[float]) -> float:
    if tolerance_for_equality:
        difference: StackValue = value_left - value_right
        return min(1.0, max(0.0, difference + tolerance_for_equality) / (2.0 * tolerance_for_equality))       # type: ignore
    if value_left >= value_right:
        return 1
    return 0


def smaller_tolerance(value_left: float, value_right: float, tolerance_for_equality: Optional[float]) -> float:
    if tolerance_for_equality:
        difference: StackValue = value_right - value_left
        return min(1.0, max(0.0, difference + tolerance_for_equality) / (2.0 * tolerance_for_equality))         # type: ignore
    if value_left <= value_right:
        return 1
    return 0


def float_not(value: float) -> float:
    assert 0 <= value <= 1
    return 1 - value


#       Standard Python precedence:
#  18     f(args…)	Function call
#       x[index:index]	Slicing
#       x[index]	Subscription
#       x.attribute	Attribute reference
#  14     **	Exponent
#       ~x	Bitwise not
#  12     +x, -x	Positive, negative
#  11     *, /, %	Product, division, remainder
#  10     +, –	Addition, subtraction
#       <<, >>	Shifts left/right
#       &	Bitwise AND
#       ^	Bitwise XOR
#       |	Bitwise OR
#  5     in, not in, is, is not, <, <=, >, >=,
#       <>, !=, ==	Comparisons, membership, identity
#  3     not x	Boolean NOT
#  2     and	Boolean AND
#  1     or	Boolean OR
OPERATORS: dict[str, Operator] = {
    'CDF': UnaryOperator(precedence=18, local_operator=local_import_cdf, name='cdf'),
    'EXP': UnaryOperator(precedence=18, local_operator=math.exp),
    'LOG': UnaryOperator(precedence=18, local_operator=math.log),
    'SUM': CombinationOperator(precedence=18, local_operator=operator.add, name='sum'),
    'ABS': UnaryOperator(precedence=18, local_operator=operator.abs),
    'FLOOR': UnaryOperator(precedence=18, local_operator=math.floor),
    'CEIL': UnaryOperator(precedence=18, local_operator=math.ceil),
    'MAX': CombinationOperator(precedence=18, local_operator=max),
    'MIN': CombinationOperator(precedence=18, local_operator=min),
    '^': BinaryOperator(precedence=14, local_operator=operator.pow, name='^'),
    '*': BinaryOperator(precedence=11, local_operator=operator.mul, name='*'),
    '/': BinaryOperator(precedence=11, local_operator=operator.truediv, name='/'),
    '+': BinaryOperator(precedence=10, local_operator=operator.add, name='+'),
    '-': BinaryOperator(precedence=10, local_operator=operator.sub, name='-'),
    '<<': ComparisonOperator(precedence=5, local_operator=smaller_tolerance, name='<<'),
    '>>': ComparisonOperator(precedence=5, local_operator=bigger_tolerance, name='>>'),
    '<': BinaryOperator(precedence=5, local_operator=smaller, name='<'),
    '<=': BinaryOperator(precedence=5, local_operator=smaller_equal, name='<='),
    '>': BinaryOperator(precedence=5, local_operator=bigger, name='>'),
    '>=': BinaryOperator(precedence=5, local_operator=bigger_equal, name='>='),
    'NOT': UnaryOperator(precedence=3, local_operator=float_not, name='not'),
    'AND': BinaryOperator(precedence=2, local_operator=min, name='and'),
    'OR': BinaryOperator(precedence=1, local_operator=max, name='or'),
    '(': LeftBracket(),
    ')': RightBracket(),
    ',': Separator(),
}

SPECIAL_UNARIES = {
    '-': UnaryOperator(precedence=12, local_operator=operator.neg),
    '+': UnaryOperator(precedence=12, local_operator=operator.pos)
}


OTHER_KEYWORDS = [pl.Branch, pl.BranchPositive, pl.BranchNegative, ':', ':=']


def make_split_str(keywords: Iterable[str]) -> str:
    def escape(keyword: str) -> str:
        if keyword in '*()<>^+':
            keyword = '\\' + keyword
        if keyword in {'\\+', '-'}:
            keyword = r'(?<!\de)(?<!\[)' + keyword
        return keyword

    ordered_keywords = []
    for keyword in sorted(keywords):
        if len(keyword) > 1:
            ordered_keywords.append(escape(keyword))
    for keyword in sorted(keywords):
        if len(keyword) == 1:
            ordered_keywords.append(escape(keyword))
    return '(' + '|'.join(ordered_keywords) + ')'


def is_float(value: str) -> bool:
    try:
        float(value)
        return True
    except Exception:       # pylint: disable=broad-except
        return False


FinancialProgramLine = tuple[tuple[Union[str, ql.Date], str], Tuple[str, ...]]      # Todo (2021/11): Bug in MyPy, remove Tuple after bugfix
FinancialProgramBlock = list[FinancialProgramLine]


def split_financial_program(financial_program: str) -> FinancialProgramBlock:
    def remove_junk(parts: list[str]) -> tuple[str, ...]:
        result: list[str] = []
        for entry in parts:
            entry = entry.strip()
            if entry and entry not in (':', ':='):
                result.append(entry)
        return tuple(result)

    result: FinancialProgramBlock = []
    financial_program = financial_program.replace('\n', ';')
    lines = remove_junk(financial_program.split(';'))
    line_splitter: re.Pattern[str] = re.compile(make_split_str(OTHER_KEYWORDS))
    command_splitter: re.Pattern[str] = re.compile(make_split_str(OPERATORS))
    for line in lines:
        line = re.sub(r'\s+', ' ', line)
        line_parts: tuple[str, ...] = remove_junk(line_splitter.split(line))
        if not line_parts:
            continue
        if line_parts[-1] == pl.Stop:
            line_parts += ('1', )
        command = line_parts[-1].replace(' ', '')
        command_parts_with_problematic_unary = ('*', ) + remove_junk(command_splitter.split(command)) + ('*', )
        command_parts = []
        count = 1
        while count < len(command_parts_with_problematic_unary) - 1:
            if command_parts_with_problematic_unary[count] in '+-' and \
                    command_parts_with_problematic_unary[count - 1] in OPERATORS and \
                    command_parts_with_problematic_unary[count - 1] != ')' and \
                    is_float(command_parts_with_problematic_unary[count + 1]):
                command_parts.append(command_parts_with_problematic_unary[count] + command_parts_with_problematic_unary[count + 1])
                count += 2
            else:
                command_parts.append(command_parts_with_problematic_unary[count])
                count += 1

        assert len(line_parts[:-1]) == 2, str(line_parts)
        result.append((line_parts[:-1], tuple(command_parts)))      # type: ignore[arg-type]
    return result


def get_var_from_object(variable_name: str, python_object: Any, fixing_date: ql.Date, payment_date: Optional[ql.Date], settlement_date: Optional[ql.Date]) -> tuple[Any, Any]:
    assert variable_name.count(pl.All) <= 1
    variable_name = variable_name.removeprefix('.')
    if not variable_name:
        return python_object, None
    if variable_name.startswith('['):
        key, variable_name = variable_name[1:].split(']', 1)
        if key == pl.All:
            if isinstance(python_object, dict):
                keys = list(python_object)
            else:
                keys = list(range(len(python_object)))
            result = [get_var_from_object(variable_name, python_object[key], fixing_date, payment_date, settlement_date)[0] for key in keys]
            return result, keys
        if key == pl.FixingDate:
            return python_object[fixing_date], None
        if key == pl.PayDate:
            return python_object[payment_date], None
        if key == pl.SettlementDate:
            return python_object[settlement_date], None
        try:
            number = int(key)
            return get_var_from_object(variable_name, python_object[number], fixing_date, payment_date, settlement_date)
        except Exception:           # pylint: disable=broad-except
            return get_var_from_object(variable_name, python_object[key], fixing_date, payment_date, settlement_date)
    parts = re.split(r'(\.|\[)', variable_name, 1)
    key = parts[0]
    variable_name = parts[1] + parts[2] if len(parts) == 3 else ''
    try:
        value = getattr(python_object, f'_{key}')
    except Exception as exception:                      # pylint: disable=broad-except
        if inspect.isdatadescriptor(getattr(python_object.__class__, key)):
            value = getattr(python_object, key)
        else:
            raise exception
    return get_var_from_object(variable_name, value, fixing_date, payment_date, settlement_date)


def command_to_infix(command: Iterable[str], ql_object: Union[QLInstrument, QLCoupon], local_variables: set[str], fixing_date: ql.Date, payment_date: ql.Date, settlement_date: ql.Date) -> list[Operator]:
    operators: list[Operator] = []
    for entry in command:
        last_operator = operators[-1] if operators else Separator()
        if entry in SPECIAL_UNARIES and isinstance(last_operator, (BinaryOperator, LeftBracket, Separator)):
            operators.append(SPECIAL_UNARIES[entry])
            continue
        if entry in OPERATORS:
            operators.append(OPERATORS[entry])
            continue
        if is_float(entry):
            operators.append(AppendValue(float(entry)))
            continue
        if entry.startswith('__'):
            raise ProgrammingError('Access to private variables forbidden.')
        if entry in local_variables:
            operators.append(AppendVariable(entry))
        elif entry.startswith(f'{pl.PathKey}[') and entry.endswith(']'):
            operators.append(AppendUnderlying(entry[len(pl.PathKey) + 1:-1]))
        else:
            value, __ = get_var_from_object(entry, ql_object, fixing_date, payment_date, settlement_date)
            operators.append(AppendValue(value))
    return operators


def infix_to_upn(infix_commands: list[Operator]) -> list[Operator]:
    output_stack: list[Operator] = []
    operator_stack: list[Operator] = []
    bracket_counter: int = 0
    for command in infix_commands:
        if isinstance(command, AppendOperator):
            output_stack.append(command)
        elif isinstance(command, BinaryOperator):
            while operator_stack and operator_stack[-1].precedence >= command.precedence:
                output_stack.append(operator_stack.pop(-1))
            operator_stack.append(command)
        elif isinstance(command, Separator):
            while operator_stack and not isinstance(operator_stack[-1], LeftBracket):
                output_stack.append(operator_stack.pop(-1))
            operator_stack.append(command)
        elif isinstance(command, UnaryOperator):
            while operator_stack and isinstance(operator_stack[-1], UnaryOperator) and operator_stack[-1].precedence >= command.precedence:
                output_stack.append(operator_stack.pop(-1))
            operator_stack.append(command)
        elif isinstance(command, LeftBracket):
            operator_stack.append(command)
            bracket_counter += 1
        elif isinstance(command, RightBracket):
            while not isinstance(operator_stack[-1], LeftBracket):
                output_stack.append(operator_stack.pop(-1))
            operator_stack.pop(-1)
            while operator_stack and isinstance(operator_stack[-1], UnaryOperator):
                output_stack.append(operator_stack.pop(-1))
            bracket_counter -= 1
            if bracket_counter < 0:
                raise Exception(f'Unbalanced brackets in "{flatten_commands(infix_commands)}"')
    if bracket_counter > 0:
        raise Exception(f'Unbalanced brackets in "{flatten_commands(infix_commands)}"')
    while operator_stack:
        output_stack.append(operator_stack.pop(-1))
    return output_stack


def evaluate(upn: list[Operator], variables: dict[str, StackValue], path: Path, observation: Optional[int], tolerance_for_equality: Optional[float] = None) -> StackValue:
    stack: list[StackValue] = []
    for entry in upn:
        entry(stack, variables, path, observation, tolerance_for_equality)
    assert len(stack) == 1, str(f'{flatten_commands(upn)}does not constitute an eligible command')

    return stack[0]


def flatten_commands(commands: list[Operator]) -> str:
    return ' '.join([str(command) for command in commands])


PL_CashFlows = dict[CashFlowDescriptor, list[float]]         # pylint: disable=invalid-name


# Attention:
# The class Statement and its derived ones are deliberately designed to be stateless, i.e. they do not
# contain a date. Therefore one can use them in the continuous case as well.

class Statement:
    def __init__(self, upn: list[Operator]):
        self._upn: list[Operator] = upn

    @staticmethod
    def dead(variables: dict[str, StackValue]) -> bool:
        return not variables['__alive']

    def __call__(self, variables: dict[str, StackValue], path: Path, observation: Optional[int], cash_flows: PL_CashFlows, tolerance_for_equality: Optional[float] = None) -> None:
        raise NotImplementedError


class Assignment(Statement):
    def __init__(self, upn: list[Operator], variable_name: str):
        super().__init__(upn)
        self._variable_name: str = variable_name

    def __call__(self, variables: dict[str, StackValue], path: Path, observation: Optional[int], cash_flows: PL_CashFlows, tolerance_for_equality: Optional[float] = None) -> None:
        variables[self._variable_name] = evaluate(self._upn, variables, path, observation, tolerance_for_equality)

    def __str__(self) -> str:
        return f'{self._variable_name} := {flatten_commands(self._upn)}'


class Stop(Statement):
    def __call__(self, variables: dict[str, StackValue], path: Path, observation: Optional[int], cash_flows: PL_CashFlows, tolerance_for_equality: Optional[float] = None) -> None:
        if self.dead(variables):
            return
        stop = evaluate(self._upn, variables, path, observation, tolerance_for_equality)
        assert isinstance(stop, (float, int))
        assert -1e-10 < stop < 1 + 1e-10
        variables['__alive'] *= 1 - stop            # type: ignore[operator]
        # A relevant alternative would be variables['__alive'] = max(variables['__alive'] - stop, 0.0)
        if variables['__alive'] < 1e-10:            # type: ignore[operator]
            variables['__alive'] = 0

    def __str__(self) -> str:
        return f'{pl.Stop} := {flatten_commands(self._upn)}'


@memoize
def rectify_dates(payment_date: Union[ql.Date, str, None], settlement_date: Union[ql.Date, str, None], settlement_days: Optional[int], calendar: ql.Calendar) -> Union[tuple[ql.Date, ql.Date], tuple[str, ql.Date], tuple[str, int]]:
    if isinstance(payment_date, ql.Date):
        if isinstance(settlement_date, ql.Date):
            return payment_date, settlement_date
        if settlement_date is None:
            return payment_date, calendar.advance(payment_date, settlement_days, ql.Days)
        if settlement_date == pl.Continuous:
            raise ProgrammingError()
        raise ProgrammingError()
    if payment_date is None:
        if isinstance(settlement_date, ql.Date):
            return calendar.advance(settlement_date, -settlement_days, ql.Days), settlement_date        # type: ignore[operator]
        if settlement_date is None:
            raise ProgrammingError()
        if settlement_date == pl.Continuous:
            if settlement_days:
                raise ProgrammingError
            return pl.Continuous, 0
        raise ProgrammingError()
    if payment_date == pl.Continuous:
        if isinstance(settlement_date, ql.Date):
            return pl.Continuous, settlement_date
        if settlement_date is None:
            return pl.Continuous, settlement_days
        if settlement_date == pl.Continuous:
            return pl.Continuous, 0
    raise ProgrammingError()


class PayFixed(Statement):
    def __init__(self, upn: list[Operator], yield_curve: QLYieldCurve, payment_date: Union[ql.Date, str, None], settlement_date: Union[ql.Date, str, None], settlement_days: Optional[int], sub_id: str):
        super().__init__(upn)
        self._yield_curve: QLYieldCurve = yield_curve
        self._currency: Reference = yield_curve.currency.reference
        self._pay_settle: Union[tuple[ql.Date, ql.Date], tuple[str, ql.Date], tuple[str, int]] = rectify_dates(payment_date, settlement_date, settlement_days, self._yield_curve.calendar)
        self._sub_id: str = sub_id

    def discounted_payment(self, variables: dict[str, StackValue], path: Path, observation: Optional[int], tolerance_for_equality: Optional[float] = None) -> tuple[float, ql.Date, ql.Date, ql.Date]:
        payment: float = evaluate(self._upn, variables, path, observation, tolerance_for_equality)       # type: ignore[assignment]

        if self._pay_settle[0] == pl.Continuous:
            payment_date: ql.Date = path.date_from_observation(observation, 0)
            if isinstance(self._pay_settle[1], int):
                settlement_date: ql.Date = path.date_from_observation(observation, self._pay_settle[1])
            else:
                settlement_date = self._pay_settle[1]
        else:
            payment_date = self._pay_settle[0]
            settlement_date = self._pay_settle[1]
        if observation is not None:
            fixing_date: ql.Date = path.date_from_observation(observation, 0)
        else:
            fixing_date = payment_date

        discount_factor = self._yield_curve[settlement_date]

        return discount_factor * payment, fixing_date, payment_date, settlement_date

    def __call__(self, variables: dict[str, StackValue], path: Path, observation: Optional[int], cash_flows: PL_CashFlows, tolerance_for_equality: Optional[float] = None) -> None:
        if self.dead(variables):
            return
        discounted_value, fixing_date, payment_date, settlement_date = self.discounted_payment(variables, path, observation, tolerance_for_equality)
        correction_factor: float = variables['__alive']  # type: ignore[assignment]
        cash_flows[CashFlowDescriptor(self._currency, fixing_date, payment_date, settlement_date, self._sub_id)].append(discounted_value * correction_factor)

    def __str__(self) -> str:
        return f'{pl.Pay}{{{self._currency}|{self._yield_curve.id}|{self._pay_settle[0]}|{self._pay_settle[1]}}} := {flatten_commands(self._upn)}'


class PayFixedIfDead(PayFixed):
    def __call__(self, variables: dict[str, StackValue], path: Path, observation: Optional[int], cash_flows: PL_CashFlows, tolerance_for_equality: Optional[float] = None) -> None:
        discounted_value, fixing_date, payment_date, settlement_date = self.discounted_payment(variables, path, observation, tolerance_for_equality)
        correction_factor: float = variables['__last_alive'] - variables['__alive']  # type: ignore[operator]
        cash_flows[CashFlowDescriptor(self._currency, fixing_date, payment_date, settlement_date)].append(discounted_value * correction_factor)

    def __str__(self) -> str:
        return f'{pl.PayIfDead}{{{self._currency}|{self._yield_curve.id}|{self._pay_settle[0]}|{self._pay_settle[1]}}} := {flatten_commands(self._upn)}'


class PayVariable(Statement):
    def __init__(self, upn: list[Operator], payment_date: Union[ql.Date, str, None], settlement_date: Union[ql.Date, str, None], settlement_days: Optional[int], currency: Reference, asset_name: str, second_curve: Optional[QLYieldCurve], sub_id: str):
        super().__init__(upn)
        self._currency: Reference = currency
        self._asset_name: str = asset_name
        self._second_curve: Optional[QLYieldCurve] = second_curve
        self._payment_date: Union[ql.Date, str, None] = payment_date
        self._settlement_date: Union[ql.Date, str, None] = settlement_date
        self._settlement_days: Optional[int] = settlement_days
        self._sub_id: str = sub_id

    def discounted_payment(self, variables: dict[str, StackValue], path: Path, observation: Optional[int], tolerance_for_equality: Optional[float] = None) -> tuple[float, ql.Date, ql.Date, ql.Date]:
        payment: float = evaluate(self._upn, variables, path, observation, tolerance_for_equality)       # type: ignore[assignment]

        pay_settle: Union[tuple[ql.Date, ql.Date], tuple[str, ql.Date], tuple[str, int]] = rectify_dates(self._payment_date, self._settlement_date, self._settlement_days, path.calendar)

        fixing_date: ql.Date = path.date_from_observation(observation, 0)
        if pay_settle[0] == pl.Continuous:
            payment_date: ql.Date = path.date_from_observation(observation, 0)
            if isinstance(pay_settle[1], int):
                settlement_date: ql.Date = path.date_from_observation(observation, pay_settle[1])
                discount_factor: float = path.discount_from_observation(observation, pay_settle[1], self._asset_name)       # type: ignore[arg-type]   # None was excluded
            else:
                settlement_date = pay_settle[1]
                discount_factor = path.discount_from_date(settlement_date, self._asset_name)
        else:
            payment_date = pay_settle[0]
            settlement_date = pay_settle[1]
            discount_factor = path.discount_from_date(settlement_date, self._asset_name)

        if self._second_curve is not None:
            discount_factor *= self._second_curve[settlement_date] / path.second_yield_curve[settlement_date]       # type: ignore[index, call-arg]   # None was excluded

        return discount_factor * payment, fixing_date, payment_date, settlement_date

    def __call__(self, variables: dict[str, StackValue], path: Path, observation: Optional[int], cash_flows: PL_CashFlows, tolerance_for_equality: Optional[float] = None) -> None:
        if self.dead(variables):
            return
        discounted_value, fixing_date, payment_date, settlement_date = self.discounted_payment(variables, path, observation, tolerance_for_equality)
        correction_factor: float = variables['__alive']  # type: ignore[assignment]
        cash_flows[CashFlowDescriptor(self._currency, fixing_date, payment_date, settlement_date, self._sub_id)].append(discounted_value * correction_factor)

    def __str__(self) -> str:
        return f'{pl.Pay}{{{pl.PathKey}[{self._asset_name}]|{self._currency}|{self._payment_date}|{self._settlement_date}}} := {flatten_commands(self._upn)}'


class PayVariableIfDead(PayVariable):
    def __call__(self, variables: dict[str, StackValue], path: Path, observation: Optional[int], cash_flows: PL_CashFlows, tolerance_for_equality: Optional[float] = None) -> None:
        discounted_value, fixing_date, payment_date, settlement_date = self.discounted_payment(variables, path, observation, tolerance_for_equality)
        correction_factor: float = variables['__last_alive'] - variables['__alive']        # type: ignore[operator]
        cash_flows[CashFlowDescriptor(self._currency, fixing_date, payment_date, settlement_date)].append(discounted_value * correction_factor)

    def __str__(self) -> str:
        return f'{pl.PayIfDead}{{{pl.PathDiscount}[{self._asset_name}]|{self._currency}|{self._payment_date}|{self._settlement_date}}} := {flatten_commands(self._upn)}'


class Branch(Statement):
    @property
    def else_statements(self) -> list[Statement]:
        return self._else_statements

    @property
    def then_statements(self) -> list[Statement]:
        return self._then_statements

    def __init__(self, upn: list[Operator], then_statements: list[Statement], else_statements: list[Statement]) -> None:
        super().__init__(upn)
        self._then_statements: list[Statement] = then_statements
        self._else_statements: list[Statement] = else_statements

    def __call__(self, variables: dict[str, StackValue], path: Path, observation: Optional[int], cash_flows: PL_CashFlows, tolerance_for_equality: Optional[float] = None) -> None:
        # Todo: (2020/12) Evaluation not necessary, in case of dead and no later payments if dead. However, we need to check if the additional overhead for checking does not outweigh the performance boost.
        test: float = evaluate(self._upn, variables, path, observation, tolerance_for_equality)          # type: ignore[assignment]
        if test > 1 - 1e-10:
            statements: list[Statement] = self._then_statements
        else:
            statements = self._else_statements
        for statement in statements:
            statement(variables, path, observation, cash_flows, tolerance_for_equality)

    def __str__(self) -> str:
        result: list[str] = [f'{pl.Branch} {flatten_commands(self._upn)}']
        result.extend(f'\t\t{pl.BranchPositive}\t{statement}' for statement in self._then_statements)

        result.extend(f'\t\t{pl.BranchNegative}\t{statement}' for statement in self._else_statements)

        return '\n'.join(result)


def financial_program_unroll(financial_program: FinancialProgramBlock, master_object: Union[QLInstrument, list[QLCoupon]]) -> list[tuple[int, FinancialProgramBlock]]:

    def replace_date_key(line: tuple[tuple[str, ...], tuple[str, ...]], date: Union[str, ql.Date, None], key: Union[int, str]) -> FinancialProgramLine:
        return (date, line[0][1].replace(pl.FixingIndex, str(key))), tuple(entry.replace(pl.FixingIndex, str(key)) for entry in line[1])

    expanded_financial_program: dict[int, list[list[FinancialProgramLine]]] = defaultdict(list)
    dates: list[Union[str, ql.Date]] = []
    last_line_count: int = -111111111
    for line_count, line in enumerate(financial_program):

        if isinstance(master_object, list):
            base_object: Union[QLInstrument, QLCoupon] = master_object[line_count]
        else:
            base_object = master_object

        if line[0][0] in (pl.BranchPositive, pl.BranchNegative):
            dates = [line[0][0]] * len(dates)
        elif line[0][0] == pl.Continuous:
            dates = [pl.Continuous]
            keys = [pl.Dummy]
            last_line_count = line_count
        else:
            dates, keys = get_var_from_object(line[0][0], base_object, None, None, None)
            dates = listify(dates)
            if not keys:
                keys = [pl.Dummy] * len(dates)
            last_line_count = line_count

        for date_count, (date, key) in enumerate(zip(dates, keys)):
            new_line = replace_date_key(line, date, key)
            if len(expanded_financial_program[last_line_count]) <= date_count:
                expanded_financial_program[last_line_count].append([])
            expanded_financial_program[last_line_count][date_count].append(new_line)

    unrolled_financial_program: list[tuple[int, FinancialProgramBlock]] = []
    for block_count, line_count in enumerate(sorted(expanded_financial_program)):
        for fp_list in expanded_financial_program[line_count]:
            unrolled_financial_program.append((block_count, fp_list))

    return unrolled_financial_program


def unrolled_financial_program_to_statements(unrolled_financial_program: list[tuple[int, FinancialProgramBlock]], master_object: Union[QLInstrument, list[QLCoupon]]) -> tuple[dict[ql.Date, list[Statement]], list[Statement], list[ql.Date]]:
    if not isinstance(master_object, list):
        _master_object: list[Union[QLInstrument, QLCoupon]] = [master_object] * len(unrolled_financial_program)
    else:
        _master_object = master_object      # type: ignore[assignment]
    base_object: Union[QLInstrument, QLCoupon] = _master_object[0]

    specific_statements: dict[ql.Date, list[Statement]] = defaultdict(list)
    continuous_statements: list[Statement] = []
    observation_dates: set[ql.Date] = set()
    local_variables: set[str] = set()

    def retrieve_payment_info(pay_str: str, fixing_date: ql.Date) -> tuple[Union[ql.Date, str, None], Union[ql.Date, str, None], Optional[int], Optional[QLYieldCurve], Optional[str], str]:
        parts = pay_str.split('|')
        if len(parts) not in (3, 4, 5):
            raise ProgrammingError(f'While retrieving payment information: Cannot interprete "{pay_str}"')
        if parts[0] == pl.FixingDate:
            payment_date: Union[ql.Date, str, None] = fixing_date
            settlement_days: Optional[int] = None
        elif not parts[0]:
            payment_date = None
            settlement_days = 0
        else:
            payment_date_or_settlement_days, __ = get_var_from_object(parts[0], base_object, fixing_date, None, None)
            if isinstance(payment_date_or_settlement_days, ql.Date):
                payment_date = payment_date_or_settlement_days
                settlement_days = None
            elif isinstance(payment_date_or_settlement_days, int):
                payment_date = None
                settlement_days = payment_date_or_settlement_days
            else:
                raise ProgrammingError(f'While retrieving payment information: Cannot interprete "{pay_str}"')

        if parts[1] == pl.FixingDate:
            settlement_date: Union[ql.Date, str, None] = fixing_date
        elif not parts[1]:
            settlement_days = 0
            settlement_date = None
        else:
            settlement_date_or_days, __ = get_var_from_object(parts[1], base_object, fixing_date, None, None)
            if isinstance(settlement_date_or_days, ql.Date):
                settlement_date = settlement_date_or_days
            elif isinstance(settlement_date_or_days, int):
                settlement_date = None
                settlement_days = settlement_date_or_days
            else:
                raise ProgrammingError(f'While retrieving payment information: Cannot interprete "{pay_str}"')
        if not (settlement_date or payment_date):
            raise ProgrammingError(f'While retrieving payment information: Cannot interprete "{pay_str}"')

        if parts[2].startswith(f'{pl.PathKey}[') and parts[2].endswith(']'):
            simulated_curve: Optional[str] = parts[2][len(pl.PathKey) + 1:-1]
            curve = None
        else:
            simulated_curve = None
            curve, __ = get_var_from_object(parts[2], base_object, fixing_date, None, None)
        if len(parts) >= 4 and parts[3]:
            assert not curve
            curve, __ = get_var_from_object(parts[3], base_object, fixing_date, None, None)
        sub_id = parts[4] if len(parts) == 5 else ''
        assert curve is None or isinstance(curve, QLYieldCurve)
        return payment_date, settlement_date, settlement_days, curve, simulated_curve, sub_id

    def retrieve_assignment(assigment_str: str, fixing_date: ql.Date) -> tuple[str, Union[ql.Date, str, None], Union[ql.Date, str, None], Optional[int], Optional[QLYieldCurve], Optional[str], str]:
        if assigment_str.startswith(pl.PayIfDead + '{'):
            payment_date, settlement_date, settlement_days, curve, simulated_curve, sub_id = retrieve_payment_info(assigment_str[len(pl.PayIfDead) + 1:-1], fixing_date)
            return pl.PayIfDead, payment_date, settlement_date, settlement_days, curve, simulated_curve, sub_id
        if assigment_str.startswith(pl.Pay + '{'):
            payment_date, settlement_date, settlement_days, curve, simulated_curve, sub_id = retrieve_payment_info(assigment_str[len(pl.Pay) + 1:-1], fixing_date)
            return pl.Pay, payment_date, settlement_date, settlement_days, curve, simulated_curve, sub_id
        if assigment_str != pl.Stop:
            local_variables.add(assigment_str)
        return assigment_str, None, None, None, None, None, ''

    def line_to_statement(line: FinancialProgramLine, fixing_date: Union[str, ql.Date], test_if_observation_date: bool = True) -> Statement:
        assignment_to, payment_date, settlement_date, settlement_days, curve, simulated_curve, sub_id = retrieve_assignment(line[0][1], fixing_date)
        infix: list[Operator] = command_to_infix(line[1], base_object, local_variables, fixing_date, payment_date, settlement_date)
        upn = infix_to_upn(infix)
        if test_if_observation_date:
            for command in upn:
                if isinstance(command, AppendUnderlying):
                    observation_dates.add(fixing_date)
                    break
            if simulated_curve:
                observation_dates.add(payment_date or settlement_date)
        return statement_factory(assignment_to, payment_date, settlement_date, settlement_days, curve, simulated_curve, upn, sub_id)

    def statement_factory(assignment_to: str, payment_date: Union[ql.Date, str, None], settlement_date: Union[ql.Date, str, None], settlement_days: Optional[int], curve: Optional[QLYieldCurve], simulated_curve: Optional[str], upn: list[Operator], sub_id: str) -> Statement:
        if assignment_to == pl.Stop:
            return Stop(upn)
        if assignment_to == pl.Pay:
            if simulated_curve is None:
                return PayFixed(upn, curve, payment_date, settlement_date, settlement_days, sub_id)             # type: ignore[arg-type]
            return PayVariable(upn, payment_date, settlement_date, settlement_days, base_object.currency.reference, simulated_curve, curve, sub_id)
        if assignment_to == pl.PayIfDead:
            if simulated_curve is None:
                return PayFixedIfDead(upn, curve, payment_date, settlement_date, settlement_days, sub_id)       # type: ignore[arg-type]
            return PayVariableIfDead(upn, payment_date, settlement_date, settlement_days, base_object.currency.reference, simulated_curve, curve, sub_id)
        return Assignment(upn, assignment_to)

    for line_count, block in unrolled_financial_program:
        base_object = _master_object[line_count]
        fixing_date: Union[str, ql.Date] = block[0][0][0]
        if len(block) == 1:
            statement: Statement = line_to_statement(block[0], fixing_date)
        else:
            branch_condition_infix = command_to_infix(block[0][1], base_object, local_variables, fixing_date, None, None)
            branch_condition_upn = infix_to_upn(branch_condition_infix)
            then_statements: list[Statement] = []
            else_statements: list[Statement] = []
            for line in block[1:]:
                statement = line_to_statement(line, fixing_date, test_if_observation_date=False)
                if line[0][0] == pl.BranchPositive:
                    then_statements.append(statement)
                else:
                    else_statements.append(statement)
            if fixing_date != pl.Continuous:
                observation_dates.add(fixing_date)
            statement = Branch(branch_condition_upn, then_statements, else_statements)
        if fixing_date == pl.Continuous:
            continuous_statements.append(statement)
        else:
            specific_statements[fixing_date].append(statement)

    observation_dates.discard(pl.Continuous)
    return specific_statements, continuous_statements, sorted(observation_dates)


def financial_program_to_statements(financial_program: str, master_object: Union[QLInstrument, list[QLCoupon]]) -> tuple[dict[ql.Date, list[Statement]], list[Statement], list[ql.Date], list[ql.Date]]:
    if isinstance(master_object, list):
        assert len(master_object) == len([item for item in financial_program.split('\n') if item.replace(' ', '').replace('\t', '')])
    financial_program_splitted: FinancialProgramBlock = split_financial_program(financial_program)
    unrolled_financial_program: list[tuple[int, FinancialProgramBlock]] = financial_program_unroll(financial_program_splitted, master_object)
    specific_statements, continuous_statements, observation_dates = unrolled_financial_program_to_statements(unrolled_financial_program, master_object)
    if __debug__:
        for statement in continuous_statements:
            if (isinstance(statement, PayFixed) and not isinstance(statement, PayFixedIfDead)) or (isinstance(statement, PayVariable) and not isinstance(statement, PayVariableIfDead)):
                raise ProgrammingError('Payments within a continuous observation period do not make sense!')
            if isinstance(statement, Branch):
                for sub_statement in statement.then_statements + statement.else_statements:
                    if (isinstance(sub_statement, PayFixed) and not isinstance(sub_statement, PayFixedIfDead)) or (isinstance(sub_statement, PayVariable) and not isinstance(sub_statement, PayVariableIfDead)):
                        raise ProgrammingError('Payments within a continuous observation period do not make sense!')
    non_observation_dates = set(specific_statements).difference(observation_dates)
    return specific_statements, continuous_statements, observation_dates, sorted(non_observation_dates)


def evaluate_statements(statements: list[Statement], variables: dict[str, StackValue], path: Path, observation: Optional[int], cash_flows: PL_CashFlows, tolerance_for_equality: Optional[float] = None) -> None:
    for statement in statements:
        statement(variables, path, observation, cash_flows, tolerance_for_equality)
