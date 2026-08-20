from pydantic import BaseModel
from typing import Dict

class Detection(BaseModel):
    timestamp: float
    counts: Dict[str, int]
    device_id: str