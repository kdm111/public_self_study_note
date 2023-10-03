'''
LeetCode 1283 : Find the Smallest Divisor Given a Threshold
정수 배열을 모두 같은 값으로 나누려고 한다. 
그 몫들의 합이 threshold의 값보다 더 작거나 같아야 한다.
만족하는 최소의 값을 구하라.

# sol1 443ms 45% 20.7MB 26%
'''

class Solution:
    def smallestDivisor(self, nums: list[int], threshold: int) -> int:
        l, r = 1, max(nums)
        while l <= r:
            m = (l + r) // 2
            if self.solve(nums, m) > threshold:
                l = m + 1
            else:
                r = m - 1
        return l

    def solve(self, nums, m):
        import math
        ret = 0
        for num in nums:
            ret += math.ceil(num / m)
        return ret
    
print(Solution().smallestDivisor([1,2,5,9], 6))
print(Solution().smallestDivisor([44,22,33,11,1], 5))

        