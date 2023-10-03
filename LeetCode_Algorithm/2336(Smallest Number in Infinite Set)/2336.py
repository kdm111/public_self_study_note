'''
# sol1
모든 양의 정수를 포함하는 집합이 존재한다.
popSmallest : 가장 작은 정수를 제거하고 반환한다.
addback : 숫자를 추가한다.
'''
class SmallestInfiniteSet:
    # sol1 
    def __init__(self):
        self.s = set()
        self.cur = 1
        
    def popSmallest(self) -> int:
        if self.s:
            ret = min(self.s)
            self.s.remove(ret)
            return ret
        else:
            self.cur += 1
            return self.cur - 1

    def addBack(self, num: int) -> None:
        if self.cur > num:
            self.s.add(num)