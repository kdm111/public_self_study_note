from typing import List

class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        # sol1 time limit exceeded
        # dp+dfs+bfs
        # dp를 사용해서 기존에 존재하던 최소 비용을 구하고
        # dfs를 통해서 최대한 최소 비용으로 가는 칸을 계산하며 기존 비용을 초과하면 함수 종료
        # bfs를 통해서 모든 칸을 체크하면서 최소 비용을 계산
        # m = len(grid); n = len(grid[0]); inf = 10**10000
        # dp = [[inf] * n for _ in range(m)]
        # dir = [[0,0],[0,1],[0,-1],[1,0],[-1,0]]
        # def dfs(r,c,k):
        #     if not (0 <= r < m and 0 <= c < n):
        #         return ;
        #     if dp[r][c] <= k:
        #         return ;
        #     dp[r][c] = k
        #     queue.append([r,c])
        #     dfs(r+dir[grid[r][c]][0], c+dir[grid[r][c]][1], k)
        # # 일단 0,0에서 출발해서 코스트를 들이지 않고 갈 수 있는 곳을 구함
        # from collections import deque
        # queue = deque([])
        # dfs(0,0,0)
        # while queue:
        #     r,c = queue.popleft()
        #     for i in range(1,5):
        #         newR, newC = r+dir[i][0], c+dir[i][1]
        #         temp = inf 
        #         if 0 <= newR < m and 0 <= newC < n:
        #             for i in range(1,5):
        #                 dir_r, dir_c = newR+dir[i][0], newC+dir[i][1]
        #                 if not (0 <= dir_r < m and 0 <= dir_c < n): continue
        #                 temp = min(temp, dp[dir_r][dir_c])
        #             dfs(newR, newC, temp+1)
        #     queue.append([newR, newC])
        #     if r == m-1 and c == n-1:
        #     return dp[r][c]
                    
        # sol2 5449ms 5% 3123ms 7%(코드를 보며 지울 수 있는 조건문을 삭제하면 2초 감소)
        # O(mn) O(mn)
        # m = len(grid); n = len(grid[0]); inf = 10**10000
        # dp = [[inf] * n for _ in range(m)]
        # dir = [[0,0],[0,1],[0,-1],[1,0],[-1,0]]
        # def dfs(r,c,k):
        #     if 0 <= r < m and 0 <= c < n and dp[r][c] > k:
        #         dp[r][c] = k
        #         queue.append([r,c])
        #         dfs(r+dir[grid[r][c]][0], c+dir[grid[r][c]][1], k)
        # from collections import deque
        # queue = deque([])
        # dfs(0,0,0)
        # while queue:
        #     r,c = queue.popleft()
        #     if r == m-1 and c == n-1:
        #         return dp[r][c]
        #     for i in range(1,5):
        #         newR, newC = r+dir[i][0], c+dir[i][1]
        #         if 0 <= newR < m and 0 <= newC < n:
        #             dfs(newR, newC, dp[r][c]+1)
        #     queue.append([newR, newC])

        # sol3 388ms 90%
        # 줄일 수 있는게 없는지 코드를 검토하면서 꾸준히 지움
        m = len(grid); n = len(grid[0]); inf = 10**10000
        dp = [[inf] * n for _ in range(m)]
        dir = [[0,1],[0,-1],[1,0],[-1,0]]
        def dfs(r,c,k):
            if 0 <= r < m and 0 <= c < n and dp[r][c] > k:
                dp[r][c] = k
                queue.append([r,c])
                dfs(r+dir[grid[r][c]-1][0], c+dir[grid[r][c]-1][1], k)
        queue = []
        dfs(0,0,0)
        while queue:
            r,c = queue.pop(0)
            if r == m-1 and c == n-1:
                return dp[r][c]
            for i,j in dir:
                if 0 <= r+i < m and 0 <= c+j < n:
                    dfs(r+i, c+j, dp[r][c]+1)


        
        


print(Solution().minCost([[1,1,1,1],[2,2,2,2],[1,1,1,1],[2,2,2,2]]))
temp = list(input().split(' '))

