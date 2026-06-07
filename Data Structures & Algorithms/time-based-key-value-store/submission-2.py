class TimeMap:

    def __init__(self):
        self.timestamps = defaultdict(dict)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timestamps[key].update({timestamp: value})

    def get(self, key: str, timestamp: int) -> str:
        val = timestamp
        # print(val)
        # print(self.timestamps[key])
        while val>0:
            if val in self.timestamps[key]:
                return self.timestamps[key][val]
            else:
                val -= 1
        return ""