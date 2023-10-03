from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # O(logn) O(1) 47ms 85%
        # 리트코드의 답은 [6,5,4,3,2,1],1 의 정답이 나오지 않음
        pivot_idx = 0
        if len(nums) == 1:
            return 0 if nums[0] == target else -1
        left = 0; right = len(nums)-1
        while left <= right:
            mid = left + (right-left)//2
            # 주어진 배열이 rotate
            if (mid == left or nums[mid-1] > nums[mid]) and (mid == right or nums[mid] < nums[mid+1]):
                pivot_idx = mid; break
            else:
                # 현재 위치하는 값이 오른쪽보다 크다면 오른쪽으로 이동
                if nums[mid] > nums[right]:
                    left = mid+1
                # 아니라면 위치하는 값이 더 작다면 왼쪽으로 이동
                else:
                    right = mid-1
        ans = self.binary_search(nums, 0, pivot_idx-1, target)
        if ans != -1: return ans
        return self.binary_search(nums, pivot_idx, len(nums)-1, target)


    def binary_search(self, nums, left, right, target):
        while left <= right:
            mid = left + (right-left)//2
            if nums[mid] == target:
                return mid
            else:
                if nums[mid] < target:
                    left = mid+1
                else:
                    right = mid-1
        return -1

print(Solution().search([3,4,5,6,1,2], 1))
# print(Solution().search([4,5,6,7,0,1,2], 0))

# print(Solution().search([0,1,2,3,4,5], 1))
# print(Solution().search([1,3,5], 5))
# print(Solution().search([6,5,4,3,2,1], 1))
# print(Solution().search([6,5,4,3,2,1], 1))

# print(Solution().search([2,1], 1))
# print(Solution().search([2,1], 2))


