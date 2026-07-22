from fastapi import APIRouter, HTTPException

router = APIRouter()


@router.get("/not-found")
def not_found():

    raise HTTPException(
        status_code=404,
        detail="Demo user not found",
    )


@router.get("/crash")
def crash():

    x = 10 / 0

    return x