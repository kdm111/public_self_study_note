from difflib import restore
from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # O(n^3) 마지막은 two pointer를 사용하여 n으로 줄임
        # 2145ms 21%
        if len(nums) < 4: return []

        nums.sort()
        result = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                l, r = j+1, len(nums)-1
                while l < r:
                    temp = nums[i]+nums[j]+nums[l]+nums[r]
                    if temp == target:
                        result.append((nums[i],nums[j],nums[l],nums[r]))
                        l += 1; r -= 1
                        while l < r and nums[l-1] == nums[l]:
                            l += 1
                        while l < r and nums[r] == nums[r+1]:
                            r -= 1
                    elif temp < target:
                        l += 1
                    else:
                        r -= 1
            
        return set(result)

                            


print(Solution().fourSum([2,2,2,2,2],8))
