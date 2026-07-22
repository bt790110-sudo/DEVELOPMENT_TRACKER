from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api.v1.api import api_router
from app.core.config import settings
from app.core.exceptions import register_exception_handlers
from app.core.logging import logger
from app.core.middleware import register_middleware


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Starting DevelopmentTracker API")

    yield

    logger.info("Stopping DevelopmentTracker API")


app = FastAPI(
    title=settings.APP_NAME,
    version=settings.API_VERSION,
    lifespan=lifespan,
)

register_middleware(app)
register_exception_handlers(app)
app.include_router(
    api_router,
    prefix="/api/v1",
)


@app.get("/",tags=["Root"])
def root():
    logger.info("Root endpoint accessed")

    return {
        "application": settings.APP_NAME,
        "version": settings.API_VERSION,
        "docs": "/docs",
    }