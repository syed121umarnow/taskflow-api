
import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api.v1.tasks import router as tasks_router
from app.core.config import settings
from app.core.logging import setup_logging
from app.repositories.task_repository import InMemoryTaskRepository


logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    setup_logging()

    app.state.task_repository = InMemoryTaskRepository()

    logger.info(
        "Starting %s in %s mode",
        settings.APP_NAME,
        settings.ENVIRONMENT,
    )

    yield

    logger.info("Shutting down %s", settings.APP_NAME)


app = FastAPI(
    title=settings.APP_NAME,
    description=settings.APP_DESCRIPTION,
    version=settings.APP_VERSION,
    debug=settings.DEBUG,
    lifespan=lifespan,
)


app.include_router(
    tasks_router,
    prefix="/api/v1",
)


@app.get("/health", tags=["Health"])
def health_check():
    logger.info("Health check requested")

    return {
        "status": "healthy",
        "application": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "environment": settings.ENVIRONMENT,
    }
