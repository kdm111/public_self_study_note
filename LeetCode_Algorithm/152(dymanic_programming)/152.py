from decimal import MAX_PREC
from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # sol1 brute force time exceeded
        # O(n^2) O(1)
        # if not nums:
        #     return 0
        # ans = nums[0]
        # for i in range(len(nums)):
        #     acc = 1
        #     for j in range(i, len(nums)):
        #         acc *= nums[j]
        #         ans = max(ans, acc)
        # return ans


        # sol2 O(n), O(1) 150ms 31%
        if not nums:
            return 0
        ans = nums[0]
        max_num = nums[0]; min_num = nums[0]
        # nums에 순차적으로 접근
        for curr in nums[1:]:
            # 현재 값과 맥스 * curr , 미니멈 * curr 비교해서  가장 큰 값과 미니멈 값 저장
            temp = max(curr, max_num*curr, min_num*curr)
            min_num = min(curr, max_num*curr, min_num*curr)
            max_num = temp
            ans = max(ans, max_num)
        return ans

            
            


# print(Solution().maxProduct([2,3,-2,4]))
print(Solution().maxProduct([-2,-3,-4]))
