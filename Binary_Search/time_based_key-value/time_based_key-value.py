class TimeMap:

    def __init__(self):
        self.timemap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timemap:
            self.timemap[key] = []
        self.timemap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key in self.timemap:
            values = self.timemap[key]
            left, right = 0, len(values)

            while left < right:
                mid = (left + right) // 2
                if values[mid][0] <= timestamp:
                    left = mid + 1
                else:
                    right = mid

            if left > 0:
                return values[left - 1][1]

        return ""
