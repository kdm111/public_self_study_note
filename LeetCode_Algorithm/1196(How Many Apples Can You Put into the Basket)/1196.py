'''
LeetCode 1196 : How Many Apples Can You Put into the Basket
사과를 5000개 까지 담을 수 있는 바구니가 존재한다. 
가장 많이 담을 수 있는 사과 바구니를 구하라

# sol1 111ms 53% 14MB 99.6%
가장 작은 수 부터 담는다. 
'''
class Solution:
    def maxNumberOfApples(self, units: list[int]) -> int:
        
        units.sort(); ans = 0; total = 5000
        for unit in units:
            if unit > total:
                break
            total -= unit
            ans += 1
        return ans