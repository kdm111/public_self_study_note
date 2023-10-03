'''
LeetCode 300 : Longest Increasing Subsequence

# sol1 3587ms 56% 14.2MB 39%
'''
class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        # sol1 
        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)
