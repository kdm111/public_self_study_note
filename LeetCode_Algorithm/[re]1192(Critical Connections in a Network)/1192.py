from typing import List
class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        # sol1 3694ms 52%
        # graph를 그려놓고 dfs를 통해 그래프 안의 루프를 찾는 방법
        # tarjan algorithm
        from collections import defaultdict
        self.hashMap = defaultdict(set)
        for [i,j] in connections:
            self.hashMap[i].add(j)
            self.hashMap[j].add(i)
        self.rank = [-1] * n; self.ans = []
        # depth와 현재 노드를 넣고 dfs
        self.dfs(None, 0, 0)
        return self.ans
    
    def dfs(self, prevNode, currNode, currDepth):
        self.rank[currNode] = currDepth
        minDepth = currDepth
        for node in self.hashMap[currNode]:
            if node == prevNode:
                continue
            temp = self.rank[node]
            # 해당 노드에 도달하지 못했을 경우 dfs
            if temp == -1:
                temp = self.dfs(currNode, node, currDepth+1)
            # 현재 depth보다 들어간 depth가 더 크다면 그것은 critical node
            if temp > currDepth:
                self.ans.append([currNode, node])
            else:
                minDepth = min(minDepth, temp)
        self.rank[currNode] = minDepth
        return minDepth   
print(Solution().criticalConnections(4, [[0,1],[1,2],[2,0],[1,3]]))