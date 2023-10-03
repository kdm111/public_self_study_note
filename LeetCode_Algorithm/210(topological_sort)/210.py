from collections import defaultdict
from typing import List
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # 토폴로지 정렬 dfs 
        # 그래프에 순환이 존재하는 지 확인하고 순환이 존재한다면 이를 반환한다.
        # 노드와 간선을 찾아서 이를 dfs로 따라가면서 확인한다.
        # sol1 dfs 177ms 37%
        self.d = {i : [] for i in range(numCourses)}
        for i, j in prerequisites:
            self.d[j].append(i)
        # 0: 방문하지 않음 1: 방문 중 2: 방문 완료
        self.visited = [0] * numCourses
        self.ans = []
        # 중간에 cycle을 찾게되면 
        self.findCycle = 0
        for i in range(numCourses):
            if self.findCycle == 1:
                break
            if self.visited[i] == 0:
                self.dfs(i)
        return self.ans[::-1] if self.findCycle != 1 else []

    def dfs(self, i):
        # 현재 방문중인 노드에 방문
        # 사이클이 발견되면 어느 노드의 순서가 의미없다.
        if self.visited[i] == 1:
            self.findCycle = 1
            return ;
        if self.visited[i] == 0:
            self.visited[i] = 1
            for j in self.d[i]:
                self.dfs(j)
            self.visited[i] = 2
            self.ans.append(i)
        
        pass

print(Solution().findOrder(4, [[1,0],[2,0],[3,1],[3,2]]))
print(Solution().findOrder(2, [[1,0],[0,1]]))
