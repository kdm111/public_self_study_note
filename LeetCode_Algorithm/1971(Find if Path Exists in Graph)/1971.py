'''
LeetCode 1971 : Find if Path Exists in Graph
그래프에서 정해진 n만큼 이동하면 dest에 도착할 수 있는 지 구하라

# sol1 time limit exceeded
그래프를 만든 뒤 dfs를 사용하여 순회한다.
easy문제라서 그냥 순회하면 될 줄 알았는데 안된다.

# sol2 2287ms 80% 325MB 5%
O(n+m) O(n+m) n은 노드의 개수 m은 엣지의 개수
그래프에서 한 번 방문한 노드는 그냥 지우지 않고 계속해서 visited안에 넣어두었다.
지우지 않으면 방문한 노드에서 다시 돌아오기 때문에 다음과 같은 경우에서 
  0
/  \\
1 - 2
0 1 2 
0 2 1로 같은 경로를 두 번 체크하게 된다.
따라서 한 번 방문한 노드의 경우 두 번 다시 방문하면 안된다.

'''
class Solution:
    def validPath(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:
        from collections import defaultdict
        hashMap = defaultdict(list)
        for edge in edges:
            hashMap[edge[0]].append(edge[1])
            hashMap[edge[1]].append(edge[0])
        visited = set([source])
        return True if self.solve(source, destination, n, hashMap, visited) else False
        
    def solve(self, src, dest, n, hashMap, visited):
        if n < 0:
            return False
        if src == dest:
            return True
        for i in hashMap[src]:
            if i in visited:
                continue
            n -= 1
            visited.add(i)
            if self.solve(i, dest, n, hashMap, visited):
                return True
            # sol2
            # visited.remove(i)
            n += 1
        return False
        
print(Solution().validPath(3, [[0,1],[1,2],[2,0]], 0, 2))
print(Solution().validPath(6, [[0,1],[0,2],[3,5],[5,4],[4,3]], 0, 5))
