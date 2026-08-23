# FastAPI is provided by the backend environment.
# pyright: reportMissingImports=false
from fastapi import APIRouter
from ..schemas import Detection
from ..tasks import process_detection

router = APIRouter(prefix="/api/detections", tags=["detections"])

@router.post("")
async def receive_detection(d: Detection):
    process_detection.delay(d.dict())
    return {"status": "queued"}