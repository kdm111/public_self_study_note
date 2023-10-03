from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # sol1 43ms 58%
        # ans = 0
        # for idx in range(len(nums)):
        #     if nums[idx] != val:
        #         nums[ans] = nums[idx]
        #         ans += 1
        # return ans

        # sol2 50ms 54% 16.4MB 31%
        ans = i = 0
        while i < len(nums):
            if nums[i] == val:
                nums.pop(i)
                nums.append(-1)
                ans += 1
                continue
            i += 1
        return len(nums) - ans

print(Solution().removeElement([0,1,2,2,3,0,4,2], 2))