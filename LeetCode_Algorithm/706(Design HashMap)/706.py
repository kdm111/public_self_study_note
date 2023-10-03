class MyHashMap:
    # 212ms 96%
    def __init__(self):
        self.hashMap = {}

    def put(self, key: int, value: int) -> None:
        self.hashMap[key] = value

    def get(self, key: int) -> int:

        return self.hashMap[key] if key in self.hashMap else -1

    def remove(self, key: int) -> None:
        # key 삭제는 pop
        self.hashMap.pop(key, None)
