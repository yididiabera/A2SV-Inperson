import bisect

class TimeMap:
    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""

        values = self.store[key]
        idx = bisect.bisect_right(values, (timestamp, chr(127))) - 1  # Use chr(127) to ensure correct ordering
        
        return values[idx][1] if idx >= 0 else ""
