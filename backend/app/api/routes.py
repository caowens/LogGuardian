from fastapi import APIRouter
from . import analyze

router = APIRouter(prefix="/api")
router.include_router(analyze.router, prefix="/analyze", tags=["analyze"])