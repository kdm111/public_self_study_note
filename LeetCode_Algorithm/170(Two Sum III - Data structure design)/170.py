'''
LeetCode 170 : Two Sum III - Data structure design
2sum 클래스를 만들어라

# sol1 651ms 62% 18.1MB 85%
O(nlogn) O(n)
find에서 sort후 계산한다.

# sol2 336mb 91% 18.5MB 28%
O(n) O(n) 
해쉬맵에서 find가 들어오면
a + b = c일 때 a != b일 때 b가 해쉬맵에서 존재하거나
a == b일 때 a가 2개 이상 존재할 경우 참을 리턴한다.

'''
class TwoSum:

    # def __init__(self):
    #     self.arr = []

    # def add(self, number: int) -> None:
    #     self.arr.append(number)
        
    # def find(self, value: int) -> bool:
    #     self.arr.sort()
    #     left = 0; right = len(self.arr)-1
    #     while left < right:
    #         val = self.arr[left] + self.arr[right]
    #         if val == value:
    #             return True
    #         elif val < value:
    #             left += 1
    #         else:
    #             right -= 1
    #     return False

    def __init__(self):
        self.hashMap = {}
    def add(self, number: int) -> None:
        if number in self.hashMap:
            self.hashMap[number] = 1
        else:
            self.hashMap[number] += 1
    def find(self, value: int) -> bool:
        for k in self.hashMap:
            c = value - k
            if c != k:
                if c in self.hashMap:
                    return True
            elif self.hashMap[k] >= 2:
                return True
        return False