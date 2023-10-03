from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # sol1 288ms 8%
        if target < 0: return []
        def solve(candidates, path, target, ans):
            if target < 0:
                return 
            if target == 0:
                ans.append(path); return
            for i in range(len(candidates)):
                solve(candidates[i:], path+[candidates[i]], target-candidates[i], ans)
            pass
        ans = []
        for i in range(len(candidates)):
            solve(candidates[i:], [candidates[i]], target-candidates[i], ans)
        return ans


        pass

print(Solution().combinationSum([2,3,5], 8))
