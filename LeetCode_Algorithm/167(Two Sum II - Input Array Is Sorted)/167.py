import enum
from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # sol1 280ms 25%
        # two pointer O(n) O(1) 
        # left = 0; right = len(numbers)-1
        # while left < right:
        #     totalSum = numbers[left]+numbers[right]
        #     if totalSum == target:
        #         return [left+1, right+1]
        #     elif totalSum < target:
        #         left += 1
        #     else:
        #         right -= 1


        # sol2 330ms 11%
        # dict O(n) O(n)
        # from collections import defaultdict
        # hashMap = defaultdict()
        # for i,n in enumerate(numbers):
        #     if target-n in hashMap:
        #         return [hashMap[target-n]+1, i+1]
        #     hashMap[n] = i

            

print(Solution().twoSum([2,7,11,15], 9))
print(Solution().twoSum([2,3,4], 6))
print(Solution().twoSum([-1, 0], -1))
print(Solution().twoSum([-3, 3, 4, 90], 0))
print(Solution().twoSum([3,24,50,79,88,150,345], 200))



