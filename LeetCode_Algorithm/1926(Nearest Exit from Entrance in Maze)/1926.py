'''
LeetCode 1926 : Nearest Exit from Entrance in Maze
미로에서 입구로부터 나갈 수 있는 가장 짧은 거리 찾기

# sol1 824ms 49% 15.5MB 50%
bfs
'''
class Solution:
    def nearestExit(self, maze: list[list[str]], entrance: list[int]) -> int:
        from collections import deque
        seen = set([])
        queue = deque([entrance + [0]])
        directions = [[0,1], [1,0], [0,-1],[-1,0]]
        while queue:
            [r, c, k] = queue.popleft()
            if (r,c) in seen:
                continue
            if not (r == entrance[0] and c == entrance[1]):
                if r == len(maze)-1 or r == 0:
                    return k
                if c == len(maze[0])-1 or c == 0:
                    return k
            seen.add((r,c))
            for [dr, dc] in directions:
                n_r = r + dr; n_c = c + dc
                if 0 <= n_r < len(maze) and 0 <= n_c < len(maze[0]):
                    if maze[n_r][n_c] == '.':
                        queue.append([n_r, n_c, k+1])
        return -1