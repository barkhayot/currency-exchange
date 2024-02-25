import requests
from app.db.models import Currency
from app.db.base import SessionLocal
from datetime import datetime
from app.schemas.schema import Converted
from fastapi import HTTPException
from app.constants.constants import SERVICE_URL


def update_exchange_rates():
    """Updates currency exchange rates in the database."""
    try:
        response = requests.get()
        data = response.json(SERVICE_URL)
        db = SessionLocal()
        for code, rate in data["rates"].items():
            currency = db.query(Currency).filter(Currency.code == code).first()
            if currency:
                currency.rate = rate
                currency.last_updated = datetime.utcnow()
            else:
                new_currency = Currency(
                    code=code, rate=rate, last_updated=datetime.utcnow()
                )
                db.add(new_currency)
        db.commit()
        db.close()
        return {"detail": "Exchange rates updated successfully"}
    except Exception:
        raise HTTPException(
            status_code=500, detail="Couldn't update currencies"
        )


def get_last_update_time():
    """Retrieves the timestamp of the last currency update."""
    db = SessionLocal()
    update_time = (
        db.query(Currency.last_updated)
        .order_by(Currency.last_updated.desc())
        .first()
    )
    db.close()
    if update_time is None:
        raise HTTPException(status_code=404, detail="No update time found")
    return update_time


def get_all_currency_data():
    """Retrieves all currency data from the database."""
    db = SessionLocal()
    currency_data = db.query(Currency).all()
    db.close()
    return currency_data


def convert_currency(source, target, amount):
    """Converts an amount from one currency to another."""
    db = SessionLocal()
    source_currency = (
        db.query(Currency).filter(Currency.code == source).first()
    )
    target_currency = (
        db.query(Currency).filter(Currency.code == target).first()
    )
    db.close()

    if not source_currency:
        raise HTTPException(
            status_code=400, detail=f"Source currency {source} not found"
        )
    if not target_currency:
        raise HTTPException(
            status_code=400, detail=f"Target currency {target} not found"
        )

    source_rate = source_currency.rate
    target_rate = target_currency.rate

    if source_rate == 0:
        raise HTTPException(
            status_code=400, detail="Source rate cannot be zero"
        )

    result = (amount / source_rate) * target_rate
    return Converted(
        source=source, target=target, amount=amount, result=result
    )
