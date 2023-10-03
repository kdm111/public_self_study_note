from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sol1 O(n^3) time exceeded
        # if len(nums) < 3: return []

        # ans = []
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         for k in range(j+1, len(nums)):
        #             if nums[i] + nums[j] + nums[k] == 0:
        #                 lst = [nums[i], nums[j], nums[k]]
        #                 lst.sort()
        #                 if lst not in ans:
        #                     ans.append(lst)
        # return ans

        # sol2 O(n^2) 7529ms 5%
        if len(nums) < 3: return []
        nums.sort()
        ans = []
        for idx, num in enumerate(nums):
            i, j = idx+1, len(nums)-1
            while i < j:
                temp = num + nums[i] + nums[j]
                if temp < 0:
                    i += 1
                elif temp > 0:
                    j -= 1
                elif temp == 0:
                    lst = [num, nums[i], nums[j]]
                    if lst not in ans:
                        ans.append(lst)
                    i += 1; j -= 1
        return ans
                
                
        
        

# print(Solution().threeSum([-1,0,1,2,-1,-4]))
# print(Solution().threeSum([-1, -1, 1, 0]))
print(Solution().threeSum([-1,0,1,2,-1,-4,-2,-3,3,0,4]))


    