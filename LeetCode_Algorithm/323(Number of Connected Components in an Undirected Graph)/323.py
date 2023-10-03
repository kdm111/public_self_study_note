'''
LeetCode 323 : Number of Connected Components in an Undirected Graph
무방향 그래프가 존재할 때 n노드가 존재할 때 연결된 그룹을 구하라.

# sol1 100ms 83% 15.7MB 50%
dfs로 순회하며 저장
'''
class Solution:
    def countComponents(self, n: int, edges: list[list[int]]) -> int:
        from collections import defaultdict
        graph = defaultdict(list)
        for [i, j] in edges:
            graph[i].append(j)
            graph[j].append(i)
        seen = set(); ans = 0
        for i in range(n):
            if i not in seen:
                stack = [i]
                while stack:
                    node = stack.pop()
                    if node not in seen:
                        seen.add(node)
                    else:
                        continue
                    for n in graph[node]:
                        stack.append(n)
                ans += 1
        return ans
                    