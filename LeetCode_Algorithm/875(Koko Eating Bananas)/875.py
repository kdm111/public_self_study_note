'''
LeetCode 875 : Koko Eating Bananas
바나나가 쌓여있는 정수 배열이 존재한다. h 시간 안에 경비원이 돌아온다.
시간 동안 k개의 바나나만 먹을 수 있다.
k개 보다 바나나가 적으면 다 먹지만 더 먹지는 못한다.
바나나를 다 먹고 싶지만 최대한 천천히 먹으려고 한다.
h 시간 안에 바나나를 다 먹을 수 있는 k개를 구하라 

# sol1 453ms 63% 15.4MB 96%
O(nlogk) O(1)

'''

class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:        
        l, r = 1, max(piles)
        while l < r:
            m = (l + r) // 2
            hours = self.solve(piles, m)
            print(l, m, r)
            if hours > h:
                l = m + 1
            else:
                r = m
        return l

    def solve(self, piles, m):
        import math
        ret = 0
        for pile in piles:
            ret += math.ceil(pile / m)
        print(ret)
        return ret

    

print(Solution().minEatingSpeed([3,6,7,11], 8))
print(Solution().minEatingSpeed([30,11,23,4,20], 5))
print(Solution().minEatingSpeed([30,11,23,4,20], 6))
print(Solution().minEatingSpeed([30000], 30000))


