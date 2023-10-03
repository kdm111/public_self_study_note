'''
LeetCode 198 : House Robber
정수 배열이 주어진다.
최종 합을 구해야 하는 데 이웃한 정수를 더하지 않고 nums의 최종합을 구하라

# sol1 39ms 17% 13.7MB 95%
이전합을 구해 최종합을 구하기

# sol2

'''
class Solution:
    def rob(self, nums: list[int]) -> int:
        # sol1
        # if len(nums) == 1:
        #     return nums[0]
        # arr = [0] * len(nums)
        # arr[0] = nums[0]; arr[1] = nums[1]
        # for i in range(2, len(nums)):
        #     temp = 0
        #     for j in range(0, i-1):
        #         if temp < arr[j]:
        #             temp = arr[j]
        #     arr[i] = nums[i] + temp
        # return max(arr[-1], arr[-2])

        # top down 35ms 42% 14MB 12%
        # def solve2(i):
        #     if i < 2:
        #         return nums[i]
        #     dp[i] = max(solve2(i) + nums[i], solve2(i - 1))
        #     return dp[i]
        # dp = [-1] * len(nums)
        # solve2(len(nums)-1)
        # return dp[-1]
    
        # sol3 32ms 70% 13.9MB 52%
        dp = [-1] * (len(nums) + 1)
        dp[0] = 0; dp[1] = nums[0]
        for i in range(1, len(nums)):
            dp[i+1] = max(dp[i-1] + nums[i], dp[i])
        return dp[-1]
            