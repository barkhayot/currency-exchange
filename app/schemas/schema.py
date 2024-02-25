from pydantic import BaseModel
from datetime import datetime


class Currency(BaseModel):
    id: int
    code: str
    rate: float
    last_updated: datetime


class LastUpdatedTime(BaseModel):
    last_updated: datetime


class Converted(BaseModel):
    source: str
    target: str
    amount: int
    result: float
