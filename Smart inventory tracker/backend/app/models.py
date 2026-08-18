# backend/app/models.py
from sqlalchemy import Column, Integer, String, Float, DateTime, JSON
from .db import Base
import datetime

class InventoryItem(Base):
    __tablename__ = 'inventory_items'
    id = Column(Integer, primary_key=True, index=True)
    sku = Column(String, unique=True, index=True)
    name = Column(String)
    count = Column(Integer, default=0)
    last_seen = Column(DateTime, default=datetime.datetime.utcnow)
    reorder_threshold = Column(Integer, default=5)
    history = Column(JSON, default=[])