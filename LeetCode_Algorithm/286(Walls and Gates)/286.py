from typing import List
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        # sol1 8249ms 5%
        # gerneral bfs
        # 일단 call stack 초과로 인해 재귀를 사용하면 안된다.
        # 그리고 최대한 set을 활용한 뒤 연산을 하지 않기 위해 
        # 자주 사용되는 변수는 따로 저장해야 한다.
        if not rooms:
            return []
        m = len(rooms); n = len(rooms[0])
        from collections import deque
        q = deque()
        for r in range(m):
            for c in range(n):
                if rooms[r][c] == 0:
                    q.append((r,c))

        while q:
            r, c = q.popleft()
            for dr,dc in ([0,1], [-1,0], [0,-1], [1,0]):
                newR = r+dr; newC = c+dc
                if 0 <= newR < m and 0 <= newC < n and rooms[newR][newC] > rooms[r][c]:
                    rooms[newR][newC] = rooms[r][c]+1
                    q.append((newR,newC))
        print(rooms)
print(Solution().wallsAndGates([[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]))