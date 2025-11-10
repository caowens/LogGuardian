from fastapi import APIRouter
from . import analyze, live

router = APIRouter(prefix="/api")
router.include_router(analyze.router, prefix="/analyze", tags=["analyze"])
router.include_router(live.router, prefix="/live", tags=["live"])