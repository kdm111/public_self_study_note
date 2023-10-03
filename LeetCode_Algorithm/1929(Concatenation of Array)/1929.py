from typing import List
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # sol1 88ms 92% 14.3MB 26%
        # return nums + nums

        # sol2 80ms 98% 14.2MB 66%
        ans = [0] * (len(nums) * 2)
        for i in range(len(nums)):
            ans[i] = nums[i]
            ans[i + len(nums)] = nums[i]
        return ans