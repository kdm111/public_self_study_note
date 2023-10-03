'''
LeetCode 1870: Minimum Speed to Arrive on Time
hour안에 도착해야 한다.
dist는 순서대로 건너야 하며, dist / speed가 소수점으로 나뉜다면 항상 올림으로 계산해 시간을 계산한다.
최소 정수 스피드 값을 구하라. 만약 시간안에 도착하는 것이 불가능 하다면 -1을 리턴하라.
hour는 두번째 자리까지 보장되어 있으며 스피드는 10^7을 초과하지 않는다.


list[int], float -> int

# sol1 3236ms 64% 28.6MB 23%
O(nlogk) O(1)
최소값과 최대값 사이에서 이진으로 계산

'''

class Solution:
    def minSpeedOnTime(self, dist: list[int], hour: float) -> int:
        # sol1
        if len(dist) - 1 >= hour:
            return -1
        l, r = 1, 10 ** 7
        while l < r:
            m = (l + r) // 2
            temp = self.solve(dist, m)
            if temp <= hour:
                r = m - 1
            else:
                l = m + 1
        return l
    
    def solve(self, dist, m):
        import math
        ret = 0
        for d in dist:
            ret = math.ceil(ret)
            ret += (d / m)
        return ret

# print(Solution().minSpeedOnTime([1,2], 1))
# print(Solution().minSpeedOnTime([1,2,3], 3))
# print(Solution().minSpeedOnTime([1,3,2], 6))
# print(Solution().minSpeedOnTime([1,3,2], 2.7))


l = 0; r = 99
while l < r:
    m = (l + r) // 2
    if m <= 4:
        l = m
    else:
        r = m - 1
    print(l, m, r)
    
print(l, r)