import time
from backend.app.crud import upsert_counts

if __name__ == "__main__":
    ts = time.time()
    sample = {'sku_A': 5, 'sku_B': 2, 'sku_C': 8}
    upsert_counts('seed-script', sample, ts)
    print("Seeded DB with sample SKUs.")