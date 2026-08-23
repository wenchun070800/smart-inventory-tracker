from fastapi import WebSocket
from typing import List
import asyncio
import json
from .crud import list_items

clients: List[WebSocket] = []

async def connect(ws: WebSocket):
    await ws.accept()
    clients.append(ws)

async def disconnect(ws: WebSocket):
    if ws in clients:
        clients.remove(ws)

def _current_counts_payload():
    rows = list_items()
    payload = {
        'counts': [
            {
                'sku': r.sku,
                'name': r.name,
                'count': r.count,
                'last_seen': r.last_seen.isoformat() if r.last_seen else None,
                'reorder_threshold': r.reorder_threshold,
            }
            for r in rows
        ]
    }
    return json.dumps(payload)

async def _send_to_client(ws: WebSocket, payload: str):
    try:
        await ws.send_text(payload)
    except Exception:
        await disconnect(ws)

def broadcast_counts():
    payload = _current_counts_payload()
    loop = asyncio.get_event_loop()
    for ws in list(clients):
        loop.create_task(_send_to_client(ws, payload))