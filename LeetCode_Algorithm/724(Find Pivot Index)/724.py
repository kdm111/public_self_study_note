from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # sol1 O(n^2), O(1) 시간초과
        # brute force 
        # 모든 수를 차례로 피봇으로 정한 뒤 값을 합하여 비교

        # for pivot in range(len(nums)):
        #     left, right = 0, pivot+1
        #     left_sum, right_sum = 0, 0
        #     while left < pivot:
        #         left_sum += nums[left]; left += 1
        #     while right < len(nums):
        #         right_sum += nums[right]; right += 1
            
        #     if left_sum == right_sum: return pivot
        
        # return -1

        # sol2 O(n), O(1) 166ms 86%
        leftSum = 0
        totalSum = sum(nums)
        for i in range(len(nums)):
            totalSum -= nums[i]
            if leftSum == totalSum:
                return i
            leftSum += nums[i]
        return -1


    

print(Solution().pivotIndex([-1,-1,0,1,1,0]))