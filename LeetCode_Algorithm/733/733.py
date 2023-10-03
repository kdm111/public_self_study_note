from typing import List
from collections import deque

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        # sol1 O(n) O(n) 93~136ms 65~19%
        # dfs
        color = image[sr][sc]
        q = deque()
        q.append([sr,sc])
        image[sr][sc] = newColor
        dr = [0,1,0,-1]
        dc = [1,0,-1,0]
        visited = [[sr,sc]]
        while q:
            x, y = q.pop()
            for i in range(4):
                new_x = x+dr[i];
                new_y = y+dc[i];
                if 0 <= new_x < len(image) and 0 <= new_y < len(image[0]) and [new_x, new_y] not in visited:
                    if image[new_x][new_y] == color:
                        q.append([new_x, new_y])
                        image[new_x][new_y] = newColor
                    visited.append([new_x, new_y])
        return image


print(Solution().floodFill([[0,0,0],[0,1,1]],1,1,1))