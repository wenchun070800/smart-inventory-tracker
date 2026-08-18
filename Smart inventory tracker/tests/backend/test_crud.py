import time
from backend.app.crud import upsert_counts, list_items
from backend.app.db import Base, engine
from backend.app.models import InventoryItem
import pytest

@pytest.fixture(scope='module', autouse=True)
def setup_db():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)

def test_upsert_and_list():
    ts = time.time()
    upsert_counts('edge-test', {'sku_test': 3}, ts)
    items = list_items()
    assert any(i.sku == 'sku_test' and i.count == 3 for i in items)