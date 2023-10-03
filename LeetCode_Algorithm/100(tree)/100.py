from sys import setdlopenflags
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        p_root = self.makeTree(p, 0)
        q_root = self.makeTree(q, 0)
        return self.solve(p_root, q_root)

    # sol1 O(n) O(n) 68ms 6%
    def solve(self, p, q):
        # 둘 다 None
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return self.solve(p.left, q.left) and self.solve(p.right, q.right)


    def makeTree(self, lst, idx):
        if idx >= len(lst):
            return None
        root = TreeNode(lst[idx])
        root.left = self.makeTree(lst, 2*idx+1)
        root.right = self.makeTree(lst, 2*idx+2)
        return root

print(Solution().isSameTree([1,2,3], [1,2,3]))