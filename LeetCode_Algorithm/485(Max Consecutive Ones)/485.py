class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        # 363ms 55% 14.3MB 68%
        ans = 0; temp = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                temp += 1
            else:
                ans = max(ans, temp)
                temp = 0
        ans = max(ans, temp)
        return ans
print(Solution().findMaxConsecutiveOnes([1,1,0,1,1,1]))
print(Solution().findMaxConsecutiveOnes([1,0,1,1,0,1]))
