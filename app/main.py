
from fastapi import FastAPI
from app.api.endpoints import router
from app.db.base import Base, engine

app = FastAPI(title="Currency Exchange")

app.include_router(router, tags=["Currency Operations"])

Base.metadata.create_all(bind=engine)
