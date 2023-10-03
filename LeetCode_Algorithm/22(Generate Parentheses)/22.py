from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # 39ms 42% 14.2MB 65%
        def solve(left, right, temp, ans):
            if len(temp) == 2*n:
                ans.append(temp); return
            if left < n:
                solve(left+1, right, temp + '(', ans)
            if right < left:
                solve(left, right+1, temp + ')', ans)
        ans = []
        solve(0, 0,"", ans)
        return ans

print(Solution().generateParenthesis(2))