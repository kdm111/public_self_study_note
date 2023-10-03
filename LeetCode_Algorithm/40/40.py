from curses.ascii import SO
from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # sol1 time exceeded
        # candidates.sort()
        # def solve(candidates, temp, target, ans):
        #     if sum(temp) > target:
        #         return ;
        #     if sum(temp) == target and temp not in ans:
        #         ans.append(temp); return ;
        #     for i in range(len(candidates)):
        #         solve(candidates[i+1:], temp+[candidates[i]], target, ans)
            
        # ans = []
        # for i in range(len(candidates)):
        #     solve(candidates[i+1:], [candidates[i]], target, ans)
        # return ans


        # sol2 O(2^n) 134ms 34%
        def solve(candidates, path, target, ans):
            if target < 0:
                return ;
            if target == 0:
                ans.append(path)
                return ;
            for i in range(len(candidates)):
                if i != 0 and candidates[i] == candidates[i-1]:
                    continue;
                solve(candidates[i+1:], path + [candidates[i]], target - candidates[i], ans)
        ans = []
        candidates.sort()
        solve(candidates, [], target, ans)
        return ans




# print(Solution().combinationSum2([10,1,2,7,6,1,5], 8))
# print(Solution().combinationSum2([2,5,2,1,2], 5))
print(Solution().combinationSum2([1], 1))

