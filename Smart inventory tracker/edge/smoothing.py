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
        length = len(self.window)
        return {k: int(round(v / length)) for k, v in agg.items()}

class ExpSmoother:
    def __init__(self, alpha=0.6):
        self.alpha = alpha
        self.state = {}

    def update(self, counts):
        for k, v in counts.items():
            prev = self.state.get(k, v)
            self.state[k] = int(round(self.alpha * v + (1 - self.alpha) * prev))
        for k in list(self.state):
            if k not in counts:
                self.state[k] = int(round((1 - self.alpha) * self.state[k]))
                if self.state[k] <= 0:
                    del self.state[k]
        return dict(self.state)
