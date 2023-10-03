
from typing import List

class Solution:

    def removeDuplicates(self, nums: List[int]) -> int:
        # sol1 O(n), O(n) 답 아님
        # hashMap = dict()
        # ans = [None] * len(nums)
        # front = 0; rear = len(nums)-1
        # k = 0
        # for idx in range(len(nums)):
        #     if nums[idx] in hashMap:
        #         ans[rear] = "_"
        #         rear -= 1
                
        #     else:
        #         ans[front] = nums[idx]
        #         front += 1
        #         hashMap[nums[idx]] = 1
        #         k += 1
        # nums = ans[:]
        # return k
        
        # sol1 O(n), O(1) 116~142ms 64~45%
        i = 0
        for j in range(1, len(nums)):
            if nums[i] != nums[j]:
                i += 1; nums[i] = nums[j]; 

        return i+1
        


print(Solution().removeDuplicates([1,1,1,2,2,3]))