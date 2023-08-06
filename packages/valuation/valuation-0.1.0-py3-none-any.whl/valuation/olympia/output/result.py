from __future__ import annotations

from collections import defaultdict
from typing import Any, Optional

from valuation.consts import result
from valuation.consts.global_parameters import OutputPrecision
from daa_utils.excel_io import ExcelIO, TableData, TableSheet
from valuation.global_settings import __type_checking__

if __type_checking__:
    # pylint: disable=ungrouped-imports
    from valuation.universal_output import ResultDB

REQUEST: str = 'request'
VALUATION: str = 'valuation'
ERROR: str = 'error'


def add_redemption_to_coupon(cash_flows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    updated_cashflows = []
    redemptions = list(filter(lambda cashflowdict: cashflowdict[result.CashFlowType] in ['Redemption'], cash_flows))
    if redemptions:
        for cashflow in cash_flows:
            if cashflow[result.CashFlowType] == 'Coupon':
                flag_appended = False
                for redemption in redemptions:
                    if cashflow[result.SettlementDate] == redemption[result.SettlementDate] and cashflow[
                        result.PaymentDate] == \
                            redemption[result.PaymentDate] and cashflow[result.SubId] == redemption[result.SubId]:
                        cashflow[result.CashFlow] = cashflow[result.CashFlow] + redemption[result.CashFlow]
                        cashflow[result.UndiscountedCashFlow] = cashflow[result.UndiscountedCashFlow] + redemption[
                            result.UndiscountedCashFlow]
                        try:
                            cashflow[result.SinkingAmount] = cashflow[result.SinkingAmount] + redemption[
                                result.SinkingAmount]
                            cashflow[result.DiscountedSinkingAmount] = redemption[
                                result.DiscountedSinkingAmount]
                        except Exception:
                            pass
                        updated_cashflows.append(cashflow)
                        flag_appended = True
                    else:
                        pass
                if not flag_appended:
                    updated_cashflows.append(cashflow)

    else:
        updated_cashflows = cash_flows

    updated_cashflows = [{key: val for key, val in sub.items() if key != result.CashFlowType} for sub in
                         updated_cashflows]
    return updated_cashflows


def convert_result_db(result_db: ResultDB) -> list[dict[str, Any]]:
    result_db_aggregated = result_db.copy(ids2cancel=("subId",))
    for result_line in result_db_aggregated:
        if result_line not in result_db and result_line.output_key not in result.OutputKeys.cash_flows:
            result_db(result_line)
    cache: dict[tuple[str, str], dict[str, Any]] = defaultdict(dict)

    for result_line in result_db:
        if result.AddedBy in result_line:
            line_key: tuple[str, str] = (result_line[result.InstrumentId], result_line[result.AddedBy])
        else:
            line_key: tuple[str, str] = (result_line[result.InstrumentId], result_line[result.InstrumentId])
        instrument_bucket: dict[str, Any] = cache[line_key]
        if REQUEST not in instrument_bucket:
            instrument_bucket[REQUEST] = {}
        if VALUATION not in instrument_bucket:
            instrument_bucket[VALUATION] = {}
        if ERROR not in instrument_bucket:
            instrument_bucket[ERROR] = {}
        valuation: dict[str, Any] = instrument_bucket[VALUATION]
        request: dict[str, Any] = instrument_bucket[REQUEST]
        errors: dict[str, Any] = instrument_bucket[ERROR]
        line_data: dict[str, Any] = result_line.data.copy()
        sub_id: str = (line_data.get(result.SubId, '') or '')
        sub_id = sub_id[:1].upper() + sub_id[1:]

        for key in (result.SubId, result.AddedBy, result.ResultType):
            if key in line_data:
                del line_data[key]
        if result_line.output_key != result.OutputKeys.general:
            if result.InstrumentId in line_data:
                del line_data[result.InstrumentId]

        if result_line.output_key == result.OutputKeys.general:
            for key, value in line_data.items():
                valuation[key + sub_id] = value
        elif result_line.output_key == result.OutputKeys.cash_flows:
            cash_flows: list[dict[str, Any]] = valuation.get(result.OutputKeys.cash_flows, [])
            update: dict[str, Any] = {result.SubId: sub_id or None}
            update.update(line_data)
            update['index'] = len(cash_flows)
            cash_flows.append(update)
            valuation[result.OutputKeys.cash_flows] = cash_flows
        elif result_line.output_key == result.OutputKeys.greeks:
            key = result.OutputKeys.greeks
            greeks: list[dict[str, Any]] = valuation.get(key, [])
            line_data['subId'] = sub_id
            greeks.append(line_data)
            valuation[result.OutputKeys.greeks] = greeks
        elif result_line.output_key == result.OutputKeys.error:
            errors.update({result.InstrumentId: line_key[0], result.AddedBy: line_key[1], **line_data})
        elif result_line.output_key == result.OutputKeys.request:
            request.update({result.InstrumentId: line_key[0], result.AddedBy: line_key[1], **line_data})
        elif result_line.output_key == result.OutputKeys.market_data:
            market_data: list[dict[str, Any]] = request.get(result.OutputKeys.market_data, [])
            market_data.append(line_data)
            valuation[result.OutputKeys.market_data] = market_data
        else:
            raise NotImplementedError(f'Unknown output key: {result_line.output_key}')

    for value in cache.values():
        if value[VALUATION]:
            if result.OutputKeys.cash_flows in value[VALUATION]:
                value[VALUATION][result.OutputKeys.cash_flows] = add_redemption_to_coupon(
                    value[VALUATION][result.OutputKeys.cash_flows])

    output: list[dict[str, Any]] = []
    for line_key, bucket in cache.items():
        if not bucket[REQUEST]:
            del bucket[REQUEST]
        if not bucket[VALUATION]:
            del bucket[VALUATION]
        if not bucket[ERROR]:
            del bucket[ERROR]
        else:
            if VALUATION in bucket:
                del bucket[VALUATION]
        output.append(bucket)
    return output


def result_to_writer(data: list[dict[str, Any]], no_test: bool = True,
                     precision: Optional[int] = OutputPrecision) -> ExcelIO:
    pv_results: list[dict[str, Any]] = []
    cash_flow_results: list[dict[str, Any]] = []
    for item in data:
        sub_data: dict[str, Any] = item.get(REQUEST, item.get(ERROR, {}))
        identifier = item.get(VALUATION, item.get(ERROR, {})).get(result.InstrumentId, 'undefined')

        for sub_key, sub_value in item.get(VALUATION, {}).items():
            if sub_key == 'cashFlows':
                for sub_item in sub_value:
                    if not isinstance(sub_item, dict):
                        continue
                    sub_item['requestId'] = identifier
                    cash_flow_results.append(sub_item)
                continue
            if sub_key == 'marketData':
                sub_value = '#'.join([
                    '|'.join([
                        f'{key}:{value}' for key, value in sub_item.items()
                    ]) for sub_item in sub_value
                ])
            sub_data[sub_key] = sub_value
        if ERROR in item:
            sub_data[ERROR] = item[ERROR]['error']
        pv_results.append(sub_data)
    writer = ExcelIO(log_io=no_test)
    if pv_results:
        pv_table = TableData(precision=precision)
        pv_table.add_data_standard(pv_results)
        pv_sheet = TableSheet('pV')
        pv_sheet.set_single(pv_table)
        writer[pv_sheet.name] = pv_sheet
    if cash_flow_results:
        cash_flow_table = TableData(precision=precision)
        cash_flow_table.add_data_standard(cash_flow_results)
        cash_flow_table.move_to_to_end('requestId')
        cash_flow_sheet = TableSheet('cashFlows')
        cash_flow_sheet.set_single(cash_flow_table)
        writer[cash_flow_sheet.name] = cash_flow_sheet
    return writer
