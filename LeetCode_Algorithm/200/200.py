from typing import List

class Solution:
    # 515ms 26%
    def numIslands(self, grid: List[List[str]]) -> int:
        ans = 0
        for c in range(len(grid[0])):
            for r in range(len(grid)):
                if grid[r][c] == '1':
                    ans += 1
                    self.solve(grid, r, c)
        return ans

    def solve(self, grid, r, c):
        dr = [0, 1, 0, -1]
        dc = [1, 0, -1, 0]
        grid[r][c] = '0'
        for i in range(4):
            r_idx = r + dr[i]
            c_idx = c + dc[i]
            if 0 <= r_idx < len(grid) and 0 <= c_idx < len(grid[0]):
                if grid[r_idx][c_idx] == '1':
                    self.solve(grid, r_idx, c_idx)

print(Solution().numIslands([
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","1"]
]))