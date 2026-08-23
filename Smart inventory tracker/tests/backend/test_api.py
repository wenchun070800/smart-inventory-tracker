from fastapi.testclient import TestClient
from backend.app.main import app

client = TestClient(app)

def test_items_endpoint():
    resp = client.get("/api/items")
    assert resp.status_code == 200