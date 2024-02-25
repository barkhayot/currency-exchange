from fastapi import APIRouter
from app.service.currency_service import (
    update_exchange_rates,
    get_last_update_time,
    convert_currency,
    get_all_currency_data,
)
from app.schemas.schema import Currency, LastUpdatedTime, Converted
from typing import List

router = APIRouter()


@router.get("/update")
def update():
    return update_exchange_rates()


@router.get("/currency", response_model=List[Currency])
def currency():
    return get_all_currency_data()


@router.get("/updated_time", response_model=LastUpdatedTime)
def updated_time():
    return get_last_update_time()


@router.get("/convert", response_model=Converted)
def convert(source: str, target: str, amount: int):
    return convert_currency(source, target, amount)
