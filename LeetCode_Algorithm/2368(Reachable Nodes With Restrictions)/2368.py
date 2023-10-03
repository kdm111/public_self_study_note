'''
LeetCode 2368 : Reachable Nodes With Restrictions
무방향 그래프가 존재할 때 n개의 노드가 존재하고 n-1개의 엣지가 존재한다.
restricted는 도달해서는 안되는 노드이다.
0에서 시작하여 restricted에 도달하지 않고 가장 많이 방문하는 노드의 개수를 구하라.

# sol1 1698ms 79% 72.4MB 86%
0에서 부터 DFS
'''
class Solution:
    def reachableNodes(self, n: int, edges: list[list[int]], restricted: list[int]) -> int:
        def valid(node):
            return node not in seen and node not in restricted
        from collections import defaultdict
        graph = defaultdict(list)
        for [i, j] in edges:
            graph[i].append(j)
            graph[j].append(i)
        restricted = set(restricted); seen = set(); ans = 0
        stack = [0]
        while stack:
            node = stack.pop()
            ans += 1; seen.add(node)
            for n in graph[node]:
                if valid(n):
                    stack.append(n)
        return ans

print(Solution().reachableNodes(7, [[0,1],[0,2],[0,5],[0,4],[3,2],[6,5]], [4,5]))
        

        
        