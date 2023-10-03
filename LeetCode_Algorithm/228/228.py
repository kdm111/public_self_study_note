from typing import List

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:

        # sol1 O(n), O(1) 32~53ms 85~20%
        ans = []
        i = 0
        for idx in range(0, len(nums)):
            if idx+1 < len(nums) and nums[idx+1] == nums[idx] + 1:
                continue
            else:
                if idx == i:
                    ans.append(f"{nums[i]}")
                else:
                    ans.append(f"{nums[i]}->{nums[idx]}")
                i = idx+1

        return ans



print(Solution().summaryRanges([0,2,3,4,6,8,9]))