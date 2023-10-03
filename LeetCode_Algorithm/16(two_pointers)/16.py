from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # sol1 brute force time exceeded
        # O(n^3) O(1)
        # import sys
        # ans = sys.maxsize
        # for i in range(len(nums)-2):
        #     for j in range(i+1, len(nums)-1):
        #         for k in range(j+1, len(nums)):
        #             temp = nums[i]+nums[j]+nums[k]
        #             if abs(target-temp) < abs(target-ans):
        #                 ans = temp
        # return ans


        # sol2 two pointer 7975ms 13%
        # O(n^2) O(1)
        nums.sort()
        ans = nums[0]+nums[1]+nums[2]
        for idx in range(len(nums)-2):
            left = idx+1; right = len(nums)-1
            while left < right:
                temp = nums[idx]+nums[left]+nums[right]
                if abs(target-temp) < abs(target-ans):
                    ans = temp
                if temp < target:
                    left += 1
                else:
                    right -= 1
            if ans == target:
                break
        return ans


print(Solution().threeSumClosest([-1,2,1,-4], 1))
print(Solution().threeSumClosest([0,0,0], 1))
print(Solution().threeSumClosest([0,1,2], 0))

