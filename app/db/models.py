from sqlalchemy import Column, Integer, String, Float, DateTime
from app.db.base import Base


class Currency(Base):
    __tablename__ = "currency"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String, unique=True, index=True)
    rate = Column(Float)
    last_updated = Column(DateTime)
