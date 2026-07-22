from fastapi import APIRouter

from app.api.v1.error_demo import router as error_router
from app.api.v1.health import router as health_router

api_router = APIRouter()

api_router.include_router(
    health_router,
)

api_router.include_router(
    error_router,
)