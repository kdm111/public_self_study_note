from typing import List

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # sol1 678ms 69%
        if n <= 2:
            return [i for i in range(n)]
        adj = [set() for _ in range(n)]
        for start, end in edges:
            adj[start].add(end)
            adj[end].add(start)
        leaves = [i for i in range(n) if len(adj[i]) == 1]
        print(adj)
        while n > 2:
            n -= len(leaves)
            new_leaves = []
            for i in leaves:
                j = adj[i].pop()
                print(adj[j])
                adj[j].remove(i)
                if len(adj[j]) == 1: new_leaves.append(j)
            leaves = new_leaves
        return leaves

print(Solution().findMinHeightTrees(4,[[1,0],[1,2],[1,3]]))