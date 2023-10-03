from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # sol1 62ms 45%t6
        self.ans = []
        nums.sort()
        self.backtracking(nums, [])
        return self.ans
        

    def backtracking(self, nums, path):
        self.ans.append(path)
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            # print(nums[i+1:])
            self.backtracking(nums[i+1:], path+[nums[i]])
        pass

print(Solution().subsetsWithDup([1,2,2]))