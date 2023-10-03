from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # sol1 O(n), O(1) 270~360ms 68~34%
        # stack
        # stack = []
        # ans = []
        # for num in nums:
        #     if num < 0: num *= -1
        #     if len(stack)==0 or stack[-1] >= num: 
        #         stack.append(num); continue
        #     else:
        #         while stack:
        #             if stack[-1] < num:
        #                 n = stack.pop()
        #                 ans.append(n**2)
        #             else:
        #                 break
                    
        #     stack.append(num)

        # while stack:
        #     n = stack.pop()
        #     ans.append(n**2)
        # return ans

        # sol2 O(n), O(1)  236~375ms  53~30%
        # 2 pointer
        left, right = 0, len(nums)-1
        ans = [0] * len(nums)
        idx = len(nums)-1
        while 0 <= idx:
            if abs(nums[left]) <= abs(nums[right]):
                ans[idx] = nums[right]**2; right -= 1; 
            elif abs(nums[left]) > abs(nums[right]):
                ans[idx] = nums[left]**2; left += 1; 
            idx-=1
        return ans



        

print(Solution().sortedSquares([-4,-1,0,3,10]))