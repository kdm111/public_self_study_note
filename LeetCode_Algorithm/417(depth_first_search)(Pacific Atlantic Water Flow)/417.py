from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # O(mn) O(mn) 376ms 68%
        if not heights: return []
        row_length = len(heights); col_length = len(heights[0])
        pacific_ocean = set()
        atlantic_ocean = set()
        for i in range(row_length):
            pacific_ocean.add((i,0))
            atlantic_ocean.add((i,col_length-1))
        for i in range(col_length):
            pacific_ocean.add((0,i))
            atlantic_ocean.add((row_length-1, i))

        pacific_reachable = self.dfs(pacific_ocean, heights)
        atlantic_reachable = self.dfs(atlantic_ocean, heights)

        #return list(pacific_reachable.intersection(atlantic_reachable))
        # 631ms 17%
        ans = []
        for temp in pacific_reachable:
            for temp2 in atlantic_reachable:
                if temp == temp2:
                    ans.append(temp)
        return ans
    def dfs(self, ocean, heights):
        row_length = len(heights); col_length = len(heights[0])
        reachable = set()
        while ocean:
            r,c = ocean.pop()
            if (r,c) in reachable:
                continue
            reachable.add((r,c))
            for (dr,dc) in [(0,1),(1,0),(0,-1),(-1,0)]:
                new_r = r+dr; new_c = c+dc
                if 0 <= new_r < row_length and 0 <= new_c < col_length:
                    if heights[r][c] <= heights[new_r][new_c]:
                        ocean.add((new_r, new_c))
        return reachable

print(Solution().pacificAtlantic([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]))