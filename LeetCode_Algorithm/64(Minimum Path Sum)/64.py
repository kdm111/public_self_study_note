'''
LeetCode 64 : Minimum Path Sum
0,0에서 (len(grid)-1, len(grid[0])-1)까지 가는 경로의 최소합을 구하라


# sol1 time limit exceed
단순한 dfs

# sol2 96ms 94% 15.7MB 85%

dp를 사용하여 현재 위치의 위와 왼쪽을 구하면서 현재 경로에서 가장 작은 값을 취한다.

'''
class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        # sol1
        # self.dr = [1,0]
        # self.dc = [0,1]
        # import sys
        # self.ans = sys.maxsize
        # self.solve(0, 0, grid, grid[0][0])
        # return self.ans

        # sol2
        dp = [[0] * len(grid[0]) for _ in range(len(grid))]
        dp[0][0] = grid[0][0]
        for c in range(1, len(grid[0])):
            dp[0][c] = grid[0][c] + dp[0][c-1]
        for r in range(1, len(grid)):
            dp[r][0] = grid[r][0] + dp[r-1][0]
        for r in range(1, len(grid)):
            for c in range(1, len(grid[0])):
                dp[r][c] = grid[r][c] + min(dp[r-1][c], dp[r][c-1])
        return dp[len(grid)-1][len(grid[0])-1]

    def solve(self, r, c, grid, temp):
        if temp > self.ans:
            return
        if r == len(grid)-1 and c == len(grid[0])-1:
            self.ans = min(self.ans, temp)
            return 
        for i in range(2):
            newR = r+self.dr[i]
            newC = c+self.dc[i]
            if 0 <= newR < len(grid) and 0 <= newC < len(grid[0]):
                temp += grid[newR][newC]
                if temp < self.ans:
                    self.solve(newR, newC, grid, temp)
                temp -= grid[newR][newC]
'''
1 2
1 1
'''
print(Solution().minPathSum([[1,2],[1,1]]))