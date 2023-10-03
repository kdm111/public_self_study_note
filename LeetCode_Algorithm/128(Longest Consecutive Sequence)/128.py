'''
# sol1 time limit exceeded
O(n^2) O(1)

# sol2 328ms 91% 29.1MB 29%
소트 후 계산
'''
class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        # sol1
        # if not nums:
        #     return 0
        # nums = set(nums)
        # ans = 1
        # for k in nums:
        #     temp = 1; 
        #     while k+1 in nums:
        #         temp += 1
        #         k += 1
        #     ans = max(temp, ans)
        # return ans
        if not nums:
            return 0
        nums = list(set(nums))
        nums.sort(); ans = 0; temp = 1
        for i in range(1, len(nums)):
            if nums[i-1]+1 == nums[i]:
                temp += 1
            else:
                temp = 1
            ans = max(ans, temp)
        return ans 
        
'''
100 4 200 1 3 2

'''
print(Solution().longestConsecutive([1,2,4]))