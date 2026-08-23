from .db import SessionLocal
from .models import InventoryItem
import datetime

def upsert_counts(device_id: str, counts: dict, ts: float):
    db = SessionLocal()
    try:
        for sku, cnt in counts.items():
            item = db.query(InventoryItem).filter(InventoryItem.sku == sku).first()
            if item:
                item.count = cnt
                item.last_seen = datetime.datetime.utcfromtimestamp(ts)
                hist = item.history or []
                hist.append({'ts': ts, 'count': cnt})
                item.history = hist[-200:]
            else:
                item = InventoryItem(
                    sku=sku,
                    name=sku,
                    count=cnt,
                    last_seen=datetime.datetime.utcfromtimestamp(ts),
                    history=[{'ts': ts, 'count': cnt}],
                )
                db.add(item)
        db.commit()
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()

def list_items():
    db = SessionLocal()
    try:
        rows = db.query(InventoryItem).all()
        return rows
    finally:
        db.close()