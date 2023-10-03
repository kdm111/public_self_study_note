from typing import List
class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        # sol1 344ms 8% 
        # O(n^2) O(1)
        ans = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                available_value = min(self.getRowMax(grid, r, c), self.getColMax(grid, r, c))
                if grid[r][c] < available_value:
                    ans += available_value - grid[r][c]
                    grid[r][c] = available_value
        return ans

    def getRowMax(self, grid, cur_r, cur_c):
        val = grid[cur_r][cur_c]
        for c in range(len(grid)):
            if val < grid[cur_r][c]:
                val = grid[cur_r][c]
        return val

    def getColMax(self, grid, cur_r, cur_c):
        val = grid[cur_r][cur_c]
        for r in range(len(grid)):
            if val < grid[r][cur_c]:
                val = grid[r][cur_c]
        return val         

print(Solution().maxIncreaseKeepingSkyline([[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]))