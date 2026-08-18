from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from .db import Base, engine
from .models import InventoryItem
from .schemas import Detection, ItemOut
from .tasks import process_detection
from .crud import list_items
import os

app = FastAPI(title="Inventory Tracker API")
Base.metadata.create_all(bind=engine)

@app.post("/api/detections")
async def receive_detection(d: Detection):
    # enqueue for async processing
    process_detection.delay(d.dict())
    return {"status": "queued"}

@app.get("/api/items")
def api_list_items():
    rows = list_items()
    return {'items': [{'sku': r.sku, 'name': r.name, 'count': r.count, 'last_seen': r.last_seen.isoformat() if r.last_seen else None, 'reorder_threshold': r.reorder_threshold} for r in rows]}

# WebSocket endpoint for live updates
from .websocket import connect, disconnect

@app.websocket("/ws")
async def websocket_endpoint(ws: WebSocket):
    await connect(ws)
    try:
        while True:
            # keep connection alive; clients may send pings
            await ws.receive_text()
    except WebSocketDisconnect:
        await disconnect(ws)