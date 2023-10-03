'''
LeetCode 1150 : Check If a Number Is Majority Element in a Sorted Array
주어지는 배열에서 숫자가 나오는 횟수가 배열의 다수인지 확인

# sol1 63ms 69% 14.1MB 14%
# O(n) O(1)
나오는 수를 체크해서 길이의 반보다 더 큰지 체크

# sol2 33ms 97% 14MB 46%
# O(log(n)), O(1)
nums가 오름차순으로 정렬되어 있으므로 이진 탐색을 통해 타겟의 시작 인덱스를 찾는다.
그리고 target보다 하나 더 큰 수의 인덱스 즉 타겟이 끝나는 인덱스를 찾는다.
어떤 수가 배열에서 과반수가 되려면 반드시 중간 값은 타겟이 될 수 밖에 없다.
그래서 인덱스의 차이가 배열 길이의 절반보다 커야하고 중간값은 항상 타겟이 되어야 한다.
'''
from typing import List
class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        # sol1
        # cnt = 0
        # for num in nums:
        #     if num == target:
        #         cnt += 1
        # return cnt > len(nums) / 2
        # sol 1-1
        # return nums.count(target) > len(nums) // 2

        # sol2 
        low = self.binary_search(nums, target)
        high = self.binary_search(nums, target+1)
        if nums[len(nums)//2] == target and (high-low) > len(nums) // 2:
            return True
        return False

    def binary_search(self, nums, target):
        left, right = 0, len(nums)
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid+1
            else:
                right = mid
        return left

        
            
        


# print(Solution().isMajorityElement([2,4,5,5,5,5,5,6,6], 5))
# print(Solution().isMajorityElement([2,4,5,6,6], 5))
print(Solution().isMajorityElement([1,2,2], 2))
print(Solution().isMajorityElement([2,2,3], 2))
print(Solution().isMajorityElement([2,2,3], 1))
print(Solution().isMajorityElement([1,2,2,3], 2))




# print(Solution().isMajorityElement([10,100,101,101], 101))

