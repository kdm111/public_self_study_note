class TimeMap:
    # sol1 hashmap in hashmap
    # 784ms 91%
    def __init__(self):
        self.hashMap = {}
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hashMap:
            self.hashMap[key] = {value : timestamp}
        else:
            self.hashMap[key].update({value : timestamp})
    def get(self, key: str, timestamp: int) -> str:
        time = 0; ret = ""
        if key in self.hashMap:
            for key, val in self.hashMap[key].items():
                if time < val and val <= timestamp:
                    ret = key; time = val
        return ret


timeMap = TimeMap()
print(timeMap.set("key", "value", 1))
print(timeMap.get("key", 1))
print(timeMap.get("key", 3))
print(timeMap.set("key", "value2", 4))
print(timeMap.get("key", 4))



