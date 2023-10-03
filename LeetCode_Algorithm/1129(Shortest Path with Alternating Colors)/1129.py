'''
LeetCode 1129 : Shortest Path with Alternating Colors
유향 그래프가 존재하고 레드 엣지와 블루 엣지가 존재한다.
0에서 각 노드로 갈 수 있는 최소 거리를 구하라.
단 노드를 타고 가면서 레드 엣지와 블루 엣지를 번갈아가면서 진행해야 한다.

# sol1
'''
class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: list[list[int]], blueEdges: list[list[int]]) -> list[int]:
        from collections import deque, defaultdict
        queue = deque([])
        ans = [float("inf")] * n
        red_graph = defaultdict(list); blue_graph = defaultdict(list)
        for [i, j] in redEdges:
            red_graph[i].append(j)
        for [i, j] in blueEdges:
            blue_graph[i].append(j)
        for [k, v] in enumerate(red_graph):
            print(k, v)
        pass

print(Solution().shortestAlternatingPaths(3, [[0,1],[1,2]], []))