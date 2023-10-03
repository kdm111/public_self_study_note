'''
leetcode 802 : Find Eventual Safe States
더 이상 나갈 곳이 없는 노드를 terminal node라고 한다.
한 노드에서 시작하여 terminal node에 도달하는 모든 노드를 오름차순으로 리턴하라.

# sol2
-1을 표시하면서 진행하다가 사이클을 만나면 종료
사이클을 만나지 않았다면 1로 치환하면서 종료

'''
class Solution:
    def eventualSafeNodes(self, graph: list[list[int]]) -> list[int]:
        # sol1 time limit exceed
    #     self.temp = set([])
    #     for i in range(len(graph)):
    #         self.dfs(i, graph, set([i]))
    #     ans = []
    #     for i in range(len(graph)):
    #         if i not in self.temp:
    #             ans.append(i)
    #     return ans

    # def dfs(self, n, graph, visited):
    #     for a in graph[n]:
    #         if a in visited or graph[a] == [-1]:
    #             for c in visited:
    #                 graph[c] = [-1]
    #                 self.temp.add(c)
    #             return 
    #         visited.add(a)
    #         self.dfs(a, graph, visited)
    #         visited.remove(a)

        # sol2 662ms 71% 24.5MB 23%
        self.visited = [0] * len(graph)
        ans = []
        for i in range(len(graph)):
            if self.dfs(i, graph):
                ans.append(i)
        return ans

    def dfs(self, n, graph):
        if self.visited[n] == 1:
            return True
        if self.visited[n] == -1:
            return False
        self.visited[n] = -1
        for c in graph[n]:
            if not self.dfs(c, graph):
                return False
        self.visited[n] = 1
        return True
                
        

print(Solution().eventualSafeNodes([[1,2],[2,3],[5],[0],[5],[],[]]))
print(Solution().eventualSafeNodes([[1,2,3,4],[1,2],[3,4],[0,4],[]]))
print(Solution().eventualSafeNodes([[1,2,3,4],[1,2,3,4],[3,4],[4],[]]))

