# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # sol1 547ms 94%
        # O(n) O(2^d)
        # from collections import deque
        # if not root:
        #     return 0
        # queue = deque([(root, 1)])
        # while queue:
        #     node, n = queue.popleft()
        #     if not node:
        #         continue
        #     if not node.left and not node.right:
        #         return n
        #     else:
        #         queue.append((node.left, n+1))
        #         queue.append((node.right, n+1))

        # sol2 533ms 82% 50.5MB 70%
        if not root:
            return 0
        self.ans = 9999999
        self.solve(root, 1)
        return self.ans
    def solve(self, node, depth):
        if not node or depth >= self.ans:
            return ;
        if not node.left and not node.right:
            self.ans = min(self.ans, depth)
            return ;
        self.solve(node.left, depth+1)
        self.solve(node.right, depth+1)
        
                
