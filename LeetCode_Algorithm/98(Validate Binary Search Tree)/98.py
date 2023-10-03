class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        rootNode = self.makeTree(root, 0)
        import math
        stack = [(rootNode, -math.inf, math.inf)]
        # preorder 57ms 69%
        while stack:
            node, lower, upper = stack.pop()
            if not node:
                continue
            if node.val <= lower or node.val >= upper:
                return False
            stack.append((node.right, node.val, upper))
            stack.append((node.left, lower, node.val))
        return True


    def makeTree(self, root, idx):
        rootNode = TreeNode(root[idx])
        if 2*idx+1 < len(root) and root[2*idx+1] != None: rootNode.left = self.makeTree(root,2*idx+1)
        if 2*idx+2 < len(root) and root[2*idx+2] != None: rootNode.right = self.makeTree(root,2*idx+2)
        return rootNode


# print(Solution().isValidBST([2,1,3]))
print(Solution().isValidBST([0,None,-1]))
# print(Solution().isValidBST([5,1,4,None,None,3,6]))
