from typing import List

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # sol1 dfs O(n^2) O(n) : visited size 300ms 54%
        ans = 0; visited = set()
        def solve(idx):
            for i in range(len(isConnected[idx])):
                if isConnected[idx][i] == 1 and i not in visited:
                    visited.add(i)
                    solve(i)
        for i in range(len(isConnected)):
            if i not in visited:
                visited.add(i)
                ans += 1
                solve(i)
        return ans

print(Solution().findCircleNum([[1,1,0],[1,1,0],[0,0,1]]))
print(Solution().findCircleNum([[1,0,0],[0,1,0],[0,0,1]]))
