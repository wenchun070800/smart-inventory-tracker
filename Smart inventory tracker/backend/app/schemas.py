from pydantic import BaseModel
from typing import Dict, Any, List

class Detection(BaseModel):
    timestamp: float
    counts: Dict[str, int]
    device_id: str

class ItemOut(BaseModel):
    sku: str
    name: str
    count: int
    last_seen: str
    reorder_threshold: int