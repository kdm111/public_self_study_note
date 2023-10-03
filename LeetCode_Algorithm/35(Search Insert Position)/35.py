from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # sol1 O(logn) 41ms 98%
        left, right = 0, len(nums)-1
        while left <= right:
            mid = left+ (right-left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid
            else:
                left = mid + 1
        return left


        # sol2 O(nlogn) 58ms 75%
        if target in nums:
            return nums.index(target)
        else:
            nums.append(target)
            nums.sort()
            return nums.index(target)


# print(Solution().searchInsert([1,3], 2))
print(Solution().searchInsert([1,3,5,7], 9))
