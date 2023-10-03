# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
from typing import List
class Solution:
    def makeTree(self, lst, idx):
        if idx >= len(lst):
            return None
        root = TreeNode(lst[idx])
        root.left = self.makeTree(lst, 2*idx+1)
        root.right = self.makeTree(lst, 2*idx+2)
        return root

    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        # sol1 49ms 71%
        # graph로 만든 뒤에 target과 k를 넣어서 거리를 측정
        graph = {}; self.visited = []; self.ans = []
        if not root:
            return []
        # self.makeGraph(root, graph)
        # self.solve(target, graph, k)
        # return self.ans

        # sol2 33ms 98%
        # annotate parent
        # node에 부모 속성을 줘서 문제 해결
        # self.par(root, None)        
        # from collections import deque
        # queue = deque([(target, k)])
        # visited = set([target])
        # while queue:
        #     node, k = queue.popleft()
        #     if k == 0:
        #         return [node.val]+[node.val for node, cnt in queue if cnt == 0]
        #     for node in [node.left, node.right, node.par]:
        #         if node and node not in visited:
        #             visited.add(node)
        #             queue.append((node, k-1))
        # return [] 
        # 

        # sol3 35ms 86% 14.5MB 11%
        def dfs(node, parent):
            if not node:
                return ;
            node.parent = parent
            dfs(node.left, node)
            dfs(node.right, node)
        dfs(root, None)
        from collections import deque
        queue = deque([target])
        seen = set([target]); dist = 0
        while queue and dist < k:
            l = len(queue)
            for _ in range(l):
                node = queue.popleft()
                for n in [node.left, node.right, node.parent]:
                    if n and n not in seen:
                        queue.append(n)
                        seen.add(n)
            dist += 1
        return [node.val for node in queue]


    def par(self, node, par):
        if node:
            node.par = par
            self.par(node.left, node)
            self.par(node.right, node)

    def makeGraph(self, node, graph):
        if node not in graph:
            graph[node] = []
        if node.left:
            graph[node].append(node.left)
        if node.right:
            graph[node].append(node.right)
        if node.left:
            if node.left not in graph:
                graph[node.left] = [node]
            self.makeGraph(node.left, graph);
        if node.right:
            if node.right not in graph:
                graph[node.right] = [node]
            self.makeGraph(node.right, graph)

    def solve(self, node, graph, cnt):
        if not node or node.val == None or node in self.visited or cnt < 0:
            return ;
        if cnt == 0:
            self.ans.append(node.val)
            return ;
        self.visited.append(node)
        for temp_node in graph[node]:
            self.solve(temp_node, graph, cnt-1)
        return ;
        
root = Solution().makeTree([3,5,1,6,2,0,8,None,None,7,4], 0)
target = root.left
print(Solution().distanceK(root, target, 2))