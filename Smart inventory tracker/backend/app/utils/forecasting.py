import numpy as np

def simple_forecast(history, window=5):
    if not history:
        return 0
    values = [h["count"] for h in history[-window:]]
    return int(np.mean(values))