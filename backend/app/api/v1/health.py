from fastapi import APIRouter

from app.core.logging import logger

router = APIRouter()


@router.get("/health", tags=["Health"])
def health_check():
    logger.info("Health check endpoint accessed")

    return {
        "status": "healthy",
        "message": "DevelopmentTracker API is running.",
    }