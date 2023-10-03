'''
LeetCode 1995 : Count Special Quadruplets
숫자 배열이 주어질 때 이 식이 해당하는 개수 구하기
nums[a] + nums[b] + nums[c] == nums[d]
a < b < c < d

# sol1 3734ms 26% 13.8MB 67%
O(n^4) O(n)
재귀로 풀기

# sol2

'''
from typing import List
class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        # sol1
    #     self.ans = 0
    #     self.solve(nums, 0, 0, 0)
    #     return self.ans
    # def solve(self, nums, idx, cnt, temp):
    #     if cnt == 3:
    #         for i in range(idx, len(nums)):
    #             if temp == nums[i]:
    #                 self.ans += 1
    #         return ;
    #     for i in range(idx, len(nums)):
    #         temp += nums[i]
    #         self.solve(nums, i+1, cnt+1, temp)
    #         temp -= nums[i]
        # sol2
        
        
        
            
print(Solution().countQuadruplets([1,2,3,6]))
print(Solution().countQuadruplets([1,1,1,3,5]))
