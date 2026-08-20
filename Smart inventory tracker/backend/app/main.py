from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from .db import Base, engine
from .models import InventoryItem
from .tasks import process_detection
from .crud import list_items
from .schemas import Detection
from .websocket import connect, disconnect
from .api import detections, items

app = FastAPI(title="Inventory Tracker API")
Base.metadata.create_all(bind=engine)

app.include_router(detections.router)
app.include_router(items.router)

@app.websocket("/ws")
async def websocket_endpoint(ws: WebSocket):
    await connect(ws)
    try:
        while True:
            await ws.receive_text()
    except WebSocketDisconnect:
        await disconnect(ws)