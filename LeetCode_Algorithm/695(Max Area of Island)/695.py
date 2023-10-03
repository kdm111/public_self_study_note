from typing import List
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # sol1 165ms 83%
        # recursive dfs O(mn) O(mn)
    #     self.dr = [0,1,0,-1]
    #     self.dc = [1,0,-1,0]
    #     ans = 0
    #     self.seen = set()
    #     for r in range(len(grid)):
    #         for c in range(len(grid[0])):
    #             if grid[r][c] == 1:
    #                 ans = max(ans, self.dfs(grid, r,c))
    #     return ans
        # sol2 174ms 24% 14.4MB 73%
        # iterative dfs 
        def valid(r, c):
            r_check = 0 <= r < len(grid)
            c_check = 0 <= c < len(grid[0]) 
            if not (r_check and c_check):
                return False
            seen_check = (r, c) not in seen
            land_check = grid[r][c] == 1
            return seen_check and land_check
        directions = [(0,1), (1,0), (-1, 0), (0, -1)]
        seen = set(); ans = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if valid(r,c):
                    seen.add((r,c))
                    stack = [(r,c)]; temp = 0
                    while stack:
                        r, c = stack.pop()
                        temp += 1
                        for i in range(4):
                            newR = r + directions[i][0]
                            newC = c + directions[i][1]
                            if valid(newR, newC):
                                seen.add((newR, newC))
                                stack.append((newR, newC))
                    ans = max(ans, temp)
        return ans
                        



                    
        
    # def dfs(self, grid, r,c):
    #     if 0 <= r < len(grid) and 0 <= c < len(grid[0]):
    #         if (r,c) not in self.seen and grid[r][c] == 1:
    #             self.seen.add((r,c))
    #             ret = 1
    #             for i in range(4):
    #                 ret += self.dfs(grid, r+self.dr[i], c+self.dc[i])
    #             return ret
    #     return 0

print(Solution().maxAreaOfIsland([
    [0,0,1,0,0,0,0,1,0,0,0,0,0],
    [0,0,0,0,0,0,0,1,1,1,0,0,0],
    [0,1,1,0,1,0,0,0,0,0,0,0,0],
    [0,1,0,0,1,1,0,0,1,0,1,0,0],
    [0,1,0,0,1,1,0,0,1,1,1,0,0],
    [0,0,0,0,0,0,0,0,0,0,1,0,0],
    [0,0,0,0,0,0,0,1,1,1,0,0,0],
    [0,0,0,0,0,0,0,1,1,0,0,0,0]]))