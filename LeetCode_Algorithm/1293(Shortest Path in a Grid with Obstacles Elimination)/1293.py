'''
LeetCode 1293 : Shortest Path in a Grid with Obstacles Elimination
m*n의 배열이 존재할 때 (0,0)에서 (m-1, n-1)까지 장애물을 피해서 가장 최소의 거리를 구하라.
단 장애물을 최대 k개를 없앨 수 있다. 

# sol1 77ms 75% 15.4MB 68%
bfs로 순회하기, 여기서 seen에 지금까지 망가뜨린 장애물 개수가 들어가야 한다.
같은 지점에 도달하더라도 지금까지 부순 장애물 개수에 따라 답이 달라진다.

그리고 하나의 엣지 케이스를 처리하면 속도가 50% 이상으로 올라간다.
0,0에서 (m-1, n-1)까지의 블록의 수는 m + n -1개이다.
그러므로 m + n -2보다 k가 크면 항상 최단 거리로 갈 수 있게되어 계산을 하지 않아도 된다.
'''
class Solution:
    def shortestPath(self, grid: list[list[int]], k: int) -> int:
        # sol1
        from collections import deque
        seen = set((0, 0, k)); directions = [[0,1], [1,0], [0, -1], [-1, 0]]
        queue = deque([(0, 0, 0, k)]); m = len(grid); n = len(grid[0]); ans = float("inf")
        if k > m + n - 2:
            return m + n - 2
        while queue:
            r, c, cnt, del_obstacle = queue.popleft()
            if cnt >= ans:
                continue
            if r == m - 1 and c == n - 1:
                ans = min(ans, cnt); 
                continue
            for [dr, dc] in directions:
                d_r = r + dr; d_c = c + dc
                if 0 <= d_r < m and 0 <= d_c < n and (d_r, d_c, del_obstacle) not in seen:
                    seen.add((d_r, d_c, del_obstacle))
                    if grid[d_r][d_c] == 0:
                        queue.append((d_r, d_c, cnt+1, del_obstacle))
                    if grid[d_r][d_c] == 1 and del_obstacle > 0:
                        queue.append((d_r, d_c, cnt+1, del_obstacle-1))
        return ans if ans != float("inf") else -1

print(Solution().shortestPath([[0,0,0,0,0,0,0,0,0,0],[0,1,1,1,1,1,1,1,1,0],[0,1,0,0,0,0,0,0,0,0],[0,1,0,1,1,1,1,1,1,1],[0,1,0,0,0,0,0,0,0,0],[0,1,1,1,1,1,1,1,1,0],[0,1,0,0,0,0,0,0,0,0],[0,1,0,1,1,1,1,1,1,1],[0,1,0,1,1,1,1,0,0,0],[0,1,0,0,0,0,0,0,1,0],[0,1,1,1,1,1,1,0,1,0],[0,0,0,0,0,0,0,0,1,0]], 1))

# [[0,0,0,0,0,0,0,0,0,0],
#  [0,1,1,1,1,1,1,1,1,0],
#  [0,1,0,0,0,0,0,0,0,0],
#  [0,1,0,1,1,1,1,1,1,1],
#  [0,1,0,0,0,0,0,0,0,0],
#  [0,1,1,1,1,1,1,1,1,0],
#  [0,1,0,0,0,0,0,0,0,0],
#  [0,1,0,1,1,1,1,1,1,1],
#  [0,1,0,1,1,1,1,0,0,0],
#  [0,1,0,0,0,0,0,0,1,0],
#  [0,1,1,1,1,1,1,0,1,0],
#  [0,0,0,0,0,0,0,0,1,0]]