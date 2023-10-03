from typing import List
class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        # sol1 1210ms 14%
        # gerneral dfs
        # O(n) O(n)
        # 커넥션의 수가 연결해야하는 컴퓨터의 수보다 적으면 무조건 안 된다.
        if len(connections) < n-1: return -1
        from collections import defaultdict
        self.hashMap = defaultdict(list)
        for i, j in connections:
            self.hashMap[i].append(j)
            self.hashMap[j].append(i)
        ans = 0
        self.visited = set()
        for k in range(n):
            if k not in self.visited:
                self.dfs(k)
                # ans는 그래프에서 그려지는 루프의 개수 + 단일 노선
                ans += 1
        return ans-1
    # dfs를 통해 루트가 나오면 반환한다.
    def dfs(self, root):
        self.visited.add(root)
        for k in self.hashMap[root]:
            if k not in self.visited:
                self.dfs(k)
            

print(Solution().makeConnected(4, [[0,1],[0,2],[1,2]]))
print(Solution().makeConnected(6, [[0,1],[0,2],[0,3],[1,2],[1,3]]))
print(Solution().makeConnected(6, [[0,1],[0,2],[0,3],[1,2]]))

