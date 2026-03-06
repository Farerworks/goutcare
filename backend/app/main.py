import logging

from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.config import settings
from app.generated.api_v1 import router as generated_router

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

DATABASE_URL = settings.DATABASE_URL
engine = create_engine(DATABASE_URL, future=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

app = FastAPI(title="GoutCare API")


@app.on_event("startup")
async def startup() -> None:
    logger.info("Starting up the application")


@app.on_event("shutdown")
async def shutdown() -> None:
    logger.info("Shutting down the application")


app.include_router(generated_router, prefix="/api/v1")
