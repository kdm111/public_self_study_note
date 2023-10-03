# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # sol1 recursive 43ms 93%
        # return self.solve(root)

        # sol2 iterative 73ms 34%
        # from collections import deque
        # queue = deque([(0, root)])
        # ans = 0
        # while queue:
        #     temp, node = queue.popleft()
        #     ans = max(ans, temp)
        #     if node:
        #         queue.append((temp+1,node.left));
        #         queue.append((temp+1,node.right));
        # return ans

        # sol3 42ms 75% 15.4MB 82%
        # if not root:
        #     return 0
        # stack = [(root, 1)]; ans = 0
        # while stack:
        #     node, depth = stack.pop()
        #     ans = max(ans, depth)
        #     if node.left:
        #         stack.append(node.left, depth+1)
        #     if node.right:
        #         stack.append(node.right, depth+1)
        # return ans


        # sol4 54ms 76% 18.7MB 34%
        ans = 0
        while head:
            ans = max(ans, head.val + curr+val)
            curr = curr.next
            head = head.next
        return ans  
                

    def solve(self, node):
        if node is None:
            return 0
        return max(self.solve(node.left),self.solve(node.right))+1