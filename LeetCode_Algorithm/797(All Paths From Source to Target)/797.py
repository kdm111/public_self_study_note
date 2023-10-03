'''
LeetCode 797 : All Paths From Source to Target
주어진 그래프에서 도착하는 모든 경로를 구하라

# sol1 89ms 98% 15.6MB 98%
O(2^n * n) O(N)
각각의 노드의 개수는 최대 N-2이다. O(N)만큼 진행한다.
진행은 재귀로 O(N)이다.


'''

class Solution:
    def allPathsSourceTarget(self, graph: list[list[int]]) -> list[list[int]]:
        self.ans = []
        self.dfs(graph, [0])
        return self.ans
        
    def dfs(self, graph, temp):
        if temp[-1] == len(graph)-1:
            self.ans.append(temp[:])
            return
        for d in graph[temp[-1]]:
            temp.append(d)
            self.dfs(graph, temp)
            temp.pop()

print(Solution().allPathsSourceTarget([[1,2],[3],[3],[]]))
# print(Solution().allPathsSourceTarget([[4,3,1],[3,2,4],[3],[4],[]]))
