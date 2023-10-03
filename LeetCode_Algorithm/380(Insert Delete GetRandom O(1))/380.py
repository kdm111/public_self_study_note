'''
LeetCode 380 : Insert Delete GetRandom O(1)
모든 메서드를 O(1)으로 해결하는 RandomizedSet을 만들어라

각각 자료구조별 메소드 시간복잡도 : https://www.ics.uci.edu/~pattis/ICS-33/lectures/complexitypython.txt

# sol1 1119ms 41% 61.4MB 57%
미리 들어온 val이 존재하는 지 O(1)으로 찾아야 하고
O(1)으로 동작을 완료해야 한다.
또한 random도 O(1)으로 해결해야 한다.

insert
미리 들어온 val이 존재하는 지 확인하려면 hashMap을 통해
미리 저장해둔 값을 꺼내야 한다. 그리고 존재하지 않는다면 추가하면 된다.

remove
삭제를 위해선 미리 알고 있던 인덱스를 꺼내와 그 인덱스를 가장 끝의 배열값과 바꿔준다.

random
random.choice()를 통해 배열의 요소를 랜덤으로 뽑아 리턴한다.
'''
class RandomizedSet:

    def __init__(self):
        self.hashMap = {}
        self.arr = []
        

    def insert(self, val: int) -> bool:
        if val in self.hashMap:
            return False
        self.hashMap[val] = len(self.arr)
        self.arr.append(val)
        return True
        

    def remove(self, val: int) -> bool:
        if val not in self.hashMap:
            return False
        last, idx = self.arr[-1], self.hashMap[val]
        self.arr[idx], self.hashMap[last] = last, idx
        self.hashMap[self.arr[idx]] = idx
        self.arr.pop()
        del self.hashMap[val]
        return True

    def getRandom(self) -> int:
        import random
        return random.choice(self.arr)
        