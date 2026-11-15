
from fastapi import FastAPI

import logging
from app.core.config import settings
from app.core.logging import setup_logging


setup_logging()

logger = logging.getLogger(__name__)

app = FastAPI(
    title="TaskFlow API",
    description="A task management REST API built with FastAPI",
    version="1.0.0",
    debug=settings.DEBUG,
)


@app.on_event("startup")
async def startup_event():
     logger.info(
        "Starting %s in %s mode",
        settings.APP_NAME,
        settings.ENVIRONMENT,
    )


@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "application": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "environment": settings.ENVIRONMENT
    }
