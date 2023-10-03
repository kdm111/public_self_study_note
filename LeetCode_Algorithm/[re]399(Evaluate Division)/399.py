'''
LeetCode 399 : Evaluate Division
기본 방정식과 계산해야할 쿼리가 존재한다. 방정식을 바탕으로 계산할 수 있다면 계산하여 리턴하고 아니라면 -1을 리턴하라

# sol1
'''
class Solution:
    def calcEquation(self, equations: list[list[str]], values: list[float], queries: list[list[str]]) -> list[float]:
        # sol1 47ms 5% 13.8MB 92%
        from collections import defaultdict
        graph = defaultdict(dict)
        for i in range(len(equations)):
            num1, num2 = equations[i]
            graph[num1][num2] = values[i]
            graph[num2][num1] = 1 / values[i]
        def solve(query0, query1):
            if query0 not in graph:
                return -1
            seen = set([query0])
            stack = [(query0, 1)]
            while stack:
                node, val = stack.pop()
                if node == query1:
                    return val
                for neighbor in graph[node]:
                    if neighbor not in seen:
                        seen.add(neighbor)
                        stack.append((neighbor, val * graph[node][neighbor]))
            return -1

        ans = []
        for query in queries:
            ans.append(solve(query[0], query[1]))
        return ans