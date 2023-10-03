'''
LeetCode 1091 : Shortest Path in Binary Matrix
n*n 그리드가 존재한다. 최소 길이의 clear path를 구하라.
clear path란 왼쪽 위에서 시작하여 오른쪽 아래로 가는 길을 의미한다.
방문 가능한 노드는 0으로 표시되어 있다.

# sol1 795ms 33% 15.5MB 12%
bfs로 돌면서 확인


'''
class Solution:
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        if grid[0][0] == 1:
            return -1
        directions = [[0,1], [1,1], [1,0], [1,-1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]
        from collections import deque
        queue = deque([(0, 0, 1)]); seen = set((0, 0))
        while queue:
            r, c, cnt = queue.popleft()
            if r == len(grid) - 1 and c == len(grid[0]) - 1:
                return cnt
            for i in range(len(directions)):
                newR = r + directions[i][0]
                newC = c + directions[i][1]
                if 0 <= newR < len(grid) and 0 <= newC < len(grid[0]) and (newR, newC) not in seen:               
                    seen.add((newR, newC))
                    if grid[newR][newC] == 0:
                        queue.append((newR, newC, cnt+1))
        return -1
            