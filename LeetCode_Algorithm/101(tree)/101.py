# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from tempfile import tempdir
from typing import Optional

class Solution:
    def makeTree(self, root, idx):
        if idx >= len(root):
            return None
        rootNode = TreeNode(root[idx])
        rootNode.left = self.makeTree(root, 2*idx+1)
        rootNode.right = self.makeTree(root,2*idx+2)
        return rootNode

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # sol1 O(n) O(1) 46ms 68%
        from collections import deque
        queue = deque([[root, root]])
        while queue:
            temp = queue.popleft()
            p = temp[0]; q = temp[1]
            if not p and not q:
                continue
            if not p or not q:
                return False
            if p.val != q.val:
                return False
            queue.append([p.left, q.right])
            queue.append([p.right, q.left])
        return True

root = Solution().makeTree([1,2,2,3,4,4,3], 0)
# print(root.val)
print(Solution().isSymmetric(root))