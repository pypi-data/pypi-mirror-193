from __future__ import annotations

from datetime import date
from typing import TYPE_CHECKING, Optional

from valuation.consts import signatures, types
from valuation.consts import fields
from daa_utils import Log
from valuation.olympia.exception import OlympiaException
from valuation.olympia.input.market_data_connection.olympia_market_data_hub_v2.market_data_links import \
    OlympiaMarketDataHubReference
from valuation.universal_transfer import Storage, Reference, TypeKey

if TYPE_CHECKING:
    pass

EmptyTypeKey = TypeKey('s', 'Empty')


class ScheduleConversionSingleTypeBase:
    _single_type2insert: str = ''

    @classmethod
    def convert(cls, schedule_storages: tuple[Storage, ...]) -> tuple[Storage, ...]:
        typed_schedules: list[Storage] = []
        for schedule_item in schedule_storages:
            if fields.Type not in schedule_item:
                schedule_item[fields.Type] = cls._single_type2insert
            typed_schedules.append(schedule_item)
        return tuple(typed_schedules)


class ScheduleConversionGeneral(ScheduleConversionSingleTypeBase):

    @classmethod
    def convert(cls, schedule_storages: tuple[Storage, ...]) -> tuple[Storage, ...]:
        typed_storages = super().convert(schedule_storages)
        if len(typed_storages) > 0 and typed_storages[0][fields.Type] != 'General':
            general_schedule: Storage = Storage()
            general_schedule[fields.Type] = 'General'
            return (general_schedule,) + typed_storages
        return typed_storages


class ScheduleConversion(ScheduleConversionGeneral):
    type_key = fields.Schedule('')
    _single_type2insert = 'Single'


class ScheduleFloatConversion(ScheduleConversionGeneral):
    type_key = fields.Schedule('Float')
    _single_type2insert = 'SingleFloat'


class ScheduleFixedConversion(ScheduleConversionGeneral):
    type_key = fields.Schedule('Fixed')
    _single_type2insert = 'SingleFixed'


class CallScheduleConversion(ScheduleConversionSingleTypeBase):
    type_key = fields.CallSchedule
    _single_type2insert = 'SingleCall'


class OlympiaCallScheduleConversion(ScheduleConversionSingleTypeBase):
    type_key = TypeKey(types.SubStorages, 'olympiaCallSchedule')

    @classmethod
    def convert(cls, schedule_storages: tuple[Storage, ...]) -> tuple[Storage, ...]:
        schedule_storages = super().convert(schedule_storages)
        result: list[Storage] = []
        for event_storage in schedule_storages:
            if event_storage[fields.Type] == 'SINGLE':
                result.append(cls._convert_single(event_storage))
            if event_storage[fields.Type] == 'AMERICAN':
                result.append(cls._convert_american(event_storage))
        return tuple(result)

    @staticmethod
    def _convert_event(event_storage: Storage) -> Storage:
        if (event_type := event_storage[TypeKey('s', 'callPutEventType')]) == 'PUT':
            price_field: TypeKey = fields.PutPrice
        elif event_type == 'CALL':
            price_field = fields.CallPrice
        else:
            raise OlympiaException(f'Unknown event type: {event_type}')
        event: Storage = event_storage[TypeKey('o', 'event')]
        for key, value in event.items():
            event_storage[key] = value
        event_storage[price_field] = event[fields.Price]
        return event_storage

    @classmethod
    def _convert_single(cls, event_storage: Storage) -> Storage:
        event_storage = cls._convert_event(event_storage)
        event_storage[fields.Type] = 'SingleCall'
        return event_storage

    @classmethod
    def _convert_american(cls, event_storage: Storage) -> Storage:
        event_storage = cls._convert_event(event_storage)
        event_storage[fields.Type] = 'AmericanCall'
        return event_storage


ScheduleConversions: dict[TypeKey, type[ScheduleConversionSingleTypeBase]] = {
    ScheduleConversion.type_key: ScheduleConversion,
    ScheduleFixedConversion.type_key: ScheduleFixedConversion,
    ScheduleFloatConversion.type_key: ScheduleFloatConversion,
    CallScheduleConversion.type_key: CallScheduleConversion,
    OlympiaCallScheduleConversion.type_key: OlympiaCallScheduleConversion
}


class InstrumentFinalization:
    _signature_factory: dict[tuple[str, str], signatures.Signature] = {
        ('DEBT_BOND', None): signatures.instrument.flexible_bond,
        ('DEBT_BOND', 'CALLABLE'): signatures.instrument.callable_flexible_bond,
        ('FxForward', 'MTM'): signatures.instrument.fx_forward
    }

    @classmethod
    def convert(cls, mutable_storage_instrument: Storage) -> Storage:
        for type_key in mutable_storage_instrument:
            if type_key in ScheduleConversions:
                schedule: tuple[Storage, ...] = mutable_storage_instrument[type_key]  # type: ignore[assignment]
                new_schedule: tuple[Storage, ...] = ScheduleConversions[type_key].convert(schedule)
                mutable_storage_instrument[type_key] = new_schedule
            if type_key == fields.Legs:
                # for storage in mutable_storage_instrument[type_key]:  # type: ignore[union-attr]
                #     signature: Signature = storage.signature  # type: ignore[union-attr]
                #     CouponFormulaConversions.get(signature, CouponFormulaConverter).convert(storage)
                for storage in mutable_storage_instrument[type_key]:  # type: ignore[union-attr]
                    if storage[fields.Type] == signatures.coupon.cms_spread.type:
                        _process_cms_spread_index(storage)
        if TypeKey(types.SubStorages, 'olympiaCallSchedule') in mutable_storage_instrument:  # TODO: remove when Excel is removed
            mutable_storage_instrument[fields.CallSchedule] = mutable_storage_instrument[TypeKey(types.SubStorages, 'olympiaCallSchedule')]
        return cls.post_process_olympia(mutable_storage_instrument)

    @classmethod
    def post_process_olympia(cls, mutable_storage: Storage) -> Storage:
        cls._map_instrument_signature(mutable_storage)
        if TypeKey('o', 'spreadConfiguration') in mutable_storage:
            mutable_storage = _process_spread_configuration(mutable_storage)
        if mutable_storage.signature in (signatures.instrument.callable_flexible_bond,):
            if fields.StochasticProcess in mutable_storage and isinstance(mutable_storage[fields.StochasticProcess],
                                                                          OlympiaMarketDataHubReference):  # fixme: no longer needed, when csv and excel data sources as deprecated
                process: OlympiaMarketDataHubReference = mutable_storage[fields.StochasticProcess]
                new_process: OlympiaMarketDataHubReference = OlympiaMarketDataHubReference(
                    process.type, f'{process.id}#{mutable_storage.reference.id}', process.sub_type, process.uri
                )
                mutable_storage[fields.StochasticProcess] = new_process
                Log.info(f'Replaced {process} by {new_process}')
        if mutable_storage.signature in signatures.instrument.fx_forward and mutable_storage.get(TypeKey('S', 'features'), tuple())[0] == 'PLAIN_VANILLA':  # TODO : I hate this condition please find another way
            mutable_storage = _process_fx_vanilla(mutable_storage)
        return mutable_storage

    @staticmethod
    def _map_instrument_signature(mutable_storage: Storage) -> None:
        instrument_type: str = mutable_storage[fields.SubType()]
        instrument_sub_type: Optional[str] = None
        instrument_features: tuple[str, ...] = mutable_storage.get(TypeKey('S', 'features'), tuple())
        if 'CALLABLE' in instrument_features or 'PUTABLE' in instrument_features:
            instrument_sub_type = 'CALLABLE'
        elif 'MTM' in instrument_features:
            instrument_sub_type = 'MTM'

        signature = InstrumentFinalization._signature_factory.get((instrument_type, instrument_sub_type))
        if signature is not None:
            mutable_storage[fields.Type] = signature.type
            mutable_storage[fields.SubType('')] = signature.sub_type
        if 'CAP' in instrument_features or 'FLOOR' in instrument_features:
            if fields.Legs in mutable_storage:
                for leg in mutable_storage[fields.Legs]:
                    if leg[fields.Type] == signatures.coupon.floating.type:
                        leg[fields.Type] = signatures.coupon.capped_floored.type


def _process_spread_configuration(mutable_storage: Storage) -> Storage:
    def spread_interpolator_id(_discount_reference: Reference) -> Reference:
        return Reference(
            'YieldCurve',
            f'SpreadInterpolator#{spread_ref.id}#{_discount_reference.id}#{maturity.isoformat()}#{additive_factor}'
        )

    spread_config_storage: Storage = mutable_storage[TypeKey('o', 'spreadConfiguration')]  # type: ignore[assignment]
    additive_factor: float = spread_config_storage[fields.AdditiveFactor]  # type: ignore[assignment]
    if TypeKey('s', '$priceClassifier') in spread_config_storage:
        delta: float = spread_config_storage[TypeKey('f', 'bidAskDelta')]  # type: ignore[assignment]
        price_classifier: str = spread_config_storage[TypeKey('s', '$priceClassifier')]  # type: ignore[assignment]
        known_classifiers: tuple[str, ...] = ('BID', 'ASK', 'MID')
        if price_classifier.upper() not in known_classifiers:
            raise OlympiaException(f'Price classifier must be one of: {known_classifiers}')
        if price_classifier == 'ASK':
            additive_factor -= delta / 2
        elif price_classifier == 'BID':
            additive_factor += delta / 2

    spread_ref: Reference = spread_config_storage[fields.SpreadCurve]  # type: ignore[assignment]
    if not spread_ref.id:
        return mutable_storage

    if fields.Maturity in mutable_storage:
        maturity: date = mutable_storage[fields.Maturity]  # type: ignore[assignment]
    elif fields.Legs in mutable_storage:
        maturity = max([sub_storage[fields.Maturity] for sub_storage in mutable_storage[fields.Legs]])  # type: ignore
    else:
        raise OlympiaException('Instrument has no maturity or could not be determined.')

    if fields.DiscountCurve in mutable_storage:
        discount_reference: Reference = mutable_storage[fields.DiscountCurve]  # type: ignore[assignment]
        mutable_storage[fields.DiscountCurve] = spread_interpolator_id(discount_reference)
    elif fields.Legs in mutable_storage:
        found_curves: set[Reference] = set()
        for sub_storage in mutable_storage[fields.Legs]:  # type: ignore[union-attr]
            if fields.DiscountCurve not in sub_storage:  # type: ignore[operator]
                OlympiaException('Leg item has no discount curve.')
            reference: Reference = sub_storage[fields.DiscountCurve]  # type: ignore[assignment, index]
            sub_storage[fields.DiscountCurve] = spread_interpolator_id(reference)  # type: ignore[index]
            found_curves.add(reference)
        if len(found_curves) != 1:
            raise OlympiaException('No or more than one discount curve found.')
    else:
        raise OlympiaException('Instrument has no discount curve or could not be determined.')

    del mutable_storage[TypeKey('o', 'spreadConfiguration')]
    return mutable_storage


def _process_cms_spread_index(mutable_storage: Storage) -> Storage:
    if fields.IRSpreadSwapIndex in mutable_storage:
        return mutable_storage

    assert (f := fields.IRSwapIndex) in mutable_storage, f'{f} missing on CMS_SPREAD leg.'
    assert (f := fields.IRSwapIndexNegative) in mutable_storage, f'{f} missing on CMS_SPREAD leg.'
    assert (f := fields.GearingPositive) in mutable_storage, f'{f} missing on CMS_SPREAD leg.'
    assert (f := fields.GearingNegative) in mutable_storage, f'{f} missing on CMS_SPREAD leg.'

    mutable_storage[fields.IRSpreadSwapIndex] = Reference('IRSpreadIndex',
                                                          'SpreadIndex#'
                                                          f'{mutable_storage[fields.GearingPositive]}*'
                                                          f'{mutable_storage[fields.IRSwapIndex]}+'
                                                          f'{mutable_storage[fields.GearingNegative]}*'
                                                          f'{mutable_storage[fields.IRSwapIndexNegative]}')

    del mutable_storage[fields.IRSwapIndex]
    del mutable_storage[fields.IRSwapIndexNegative]
    del mutable_storage[fields.GearingPositive]
    del mutable_storage[fields.GearingNegative]
    return mutable_storage


def _process_fx_vanilla(mutable_storage_instrument: Storage) -> Storage:
    mutable_storage_instrument[fields.Type] = signatures.valuation.market_data.type
    mutable_storage_instrument[fields.SubType()] = signatures.valuation.market_data.sub_type
    mutable_storage_instrument[fields.FixingDate] = mutable_storage_instrument[fields.Maturity]
    mutable_storage_instrument[fields.MarketData] = mutable_storage_instrument[fields.FxRate]
    mutable_storage_instrument[fields.OptionalInfo] = mutable_storage_instrument[fields.BaseCurrency].id

    return mutable_storage_instrument
