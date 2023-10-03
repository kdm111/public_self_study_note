from typing import List
'''
LeetCode 523 : Continuous Subarray Sum
정수 배열과 숫자가 주어질 때 good 서브배열 존재하는지 찾아라

굿 서브배열이란 길이가 최고 2 이상이고 서브배열의 합이 k로 나누어 떨어진다.
서브 배열은 배열에서 연속적이다.

# sol1
서브 배열의 합은 n^2으로 구할 수 있다.
'''
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # sol1

        leftSum = [0] * len(nums); rightSum = [0] * len(nums)
        total = 0
        for i in range(len(nums)):
            total += nums[i]
            leftSum[i] = total
        total = 0
        for i in range(len(nums)-1, -1, -1):
            total += nums[i]
            rightSum[i] = total
        

        # hashMap = {0 : 0}; totalSum = 0
        # for i in range(len(nums)):
        #     totalSum += nums[i]
        #     if totalSum % k not in hashMap:
        #         hashMap[totalSum % k] = i + 1
        #     elif hashMap[totalSum % k] < i:
        #         return True
        # return False
            

print(Solution().checkSubarraySum([23,2,4,6,7], 6))
        
