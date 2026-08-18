from collections import deque, Counter

class SlidingWindowSmoother:
    def __init__(self, window_size=5):
        self.window_size = window_size
        self.window = deque(maxlen=window_size)

    def add(self, counts_dict):
        """
        counts_dict: {name: count}
        """
        self.window.append(counts_dict)

    def smoothed(self):
        if not self.window:
            return {}
        agg = Counter()
        for d in self.window:
            agg.update(d)
        # average across window length
        length = len(self.window)
        return {k: int(round(v / length)) for k, v in agg.items()}