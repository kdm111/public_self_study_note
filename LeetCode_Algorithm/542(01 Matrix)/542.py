from typing import List
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:

        # sol1 brute force
        # O((mn) O(mn)
    #     for r in range(len(mat)):
    #         for c in range(len(mat[0])):
    #             if mat[r][c] != 0:
    #                 self.bfs(mat, r, c)
    #     return mat
    
    # def bfs(self, mat, r, c):
    #     dr = [0,1,0,-1]
    #     dc = [1,0,-1,0]
    #     R,C = r,c
    #     from collections import deque
    #     queue = deque([(r,c,0)])
    #     seen = ((r,c))
    #     while queue:
    #         r, c, cnt = queue.popleft()
    #         if mat[r][c] == 0:
    #             mat[R][C]=cnt
    #             return ;
    #         for i in range(4):
    #             t_r = r +dr[i]; t_c = c+dc[i]
    #             if 0 <= t_r < len(mat) and 0 <= t_c < len(mat[0]):
    #                 if (t_r,t_c) not in seen:
    #                     queue.append((t_r, t_c, cnt+1))

        # sol1 1768ms 18%
        # O(mn) O(mn)
        from collections import deque
        queue = deque([])
        for r in range(len(mat)):
            for c in range(len(mat[0])):
                if mat[r][c] == 0:
                    queue.append((r,c))
                else:
                    mat[r][c] = -1

        dr = [0,1,0,-1]
        dc = [1,0,-1,0]
        while queue:
            r, c = queue.popleft()
            for i in range(4):
                tr = r+dr[i]; tc = c+dc[i]
                if tr < 0 or tr == len(mat) or tc < 0 or tc == len(mat[0]) or mat[tr][tc] != -1:
                    continue;
                mat[tr][tc] = mat[r][c] + 1
                queue.append((tr,tc))
        return mat
        
            
            