from fastapi import APIRouter
from ..crud import list_items

router = APIRouter(prefix="/api/items", tags=["items"])

@router.get("")
def get_items():
    rows = list_items()
    return {
        "items": [
            {
                "sku": r.sku,
                "name": r.name,
                "count": r.count,
                "last_seen": r.last_seen.isoformat() if r.last_seen else None,
                "reorder_threshold": r.reorder_threshold,
            }
            for r in rows
        ]
    }