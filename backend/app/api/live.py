from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from ..services.simulator import demo_stream

router = APIRouter()

@router.get("/stream")
def stream_demo():
    return StreamingResponse(demo_stream(), media_type="text/event-stream")
