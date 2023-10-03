'''
LeetCode 410 : Split Array Largest Sum
정수 배열과 정수 k가 존재한다.
정수 배열을 k개의 서브 어레이로 나누고 그 배열의 최대합을 구하라.
하지만 각각 배열의 합은 최소여야 한다. 

# sol1 40ms 69% 14MB 65%

'''
class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:
        def solve(m):
            curr_sum = 0
            splits = 0
            for num in nums:
                if curr_sum + num <= m:
                    curr_sum += num
                else:
                    curr_sum = num
                    splits += 1
            return splits + 1
        l = max(nums); r = sum(nums)
        while l <= r:
            m = (l + r) // 2
            temp = solve(m)
            if temp <= k:
                r = m - 1
                ans = m
            else:
                l = m + 1
        return ans


print(Solution().splitArray([99, 0, 0, 1, 50], 2))
print(Solution().splitArray([50, 1, 0, 0, 99], 2))
print(Solution().splitArray([50, 1, 99, 0, 6], 3))
print(Solution().splitArray([20, 40, 1, 0, 0, 20, 30], 3))
print(Solution().splitArray([99999999, 0, 0, 9, 9], 2))
print(Solution().splitArray([1], 1))
print(Solution().splitArray([1,3], 2))
print(Solution().splitArray([1,2,3,4,5,6,7], 3))
print(Solution().splitArray([7,7,7,7,7,7,7,7], 4))



