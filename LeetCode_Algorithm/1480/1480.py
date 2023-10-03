from typing import List

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:

        # sol1 O(n)
        # 54ms 65%
        # ans = []
        # temp = 0
        # for num in nums:
        #     temp += num
        #     ans.append(temp)
        # return ans


        # sol2 O(n)
        # 33ms 99%
        for idx in range(1, len(nums)):
            nums[idx] = nums[idx-1] + nums[idx]
        return nums

print(Solution().runningSum([1,2,3,4]))