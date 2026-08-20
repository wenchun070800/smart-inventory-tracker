import time
from backend.app.crud import upsert_counts

if __name__ == "__main__":
    ts = time.time()
    sample = {
        "sku_A": 10,
        "sku_B": 4,
        "sku_C": 0,
        "sku_D": 7
    }
    upsert_counts("seed-script", sample, ts)
    print("Database seeded with sample inventory counts.")