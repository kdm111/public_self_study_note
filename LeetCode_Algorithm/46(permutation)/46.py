from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # O(P(n,k))
        # 41ms 88%
        ans = []
        def backtracking(n):
            if n == len(nums):
                ans.append(nums[:])
            for idx in range(n, len(nums)):
                nums[n], nums[idx] = nums[idx], nums[n]
                backtracking(n+1)
                nums[n], nums[idx] = nums[idx], nums[n] 
        backtracking(0)
        return ans

print(Solution().permute([1,2,3]))