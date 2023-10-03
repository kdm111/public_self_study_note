# Definition for a binary tree node.
from lib2to3.pgen2.token import OP
from re import L, S
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root, targetSum: int) -> bool:
        if root == []: return False
        
        root_node = self.make_tree(root, 0)

        # O(n) 91ms 6%
        # if not root_node:
        #     return False
        # q = [(root_node, 0)]
        # while q:
        #     node, acc = q.pop()
        #     acc += node.val
        #     if not node.left and not node.right:
        #         if acc == targetSum:
        #             return True
        #     if node.right: q.append((node.right, acc))
        #     if node.left: q.append((node.left, acc))
        # return False


        # sol2 O(n) 62ms 43%
        # return self.solve(root_node, 0, targetSum)

        # sol3 86ms 32%
        return self.dfs(root, targetSum)
    
    def dfs(self, node, targetSum):
        if node:
            targetSum -= node.val
            if not node.left and not node.right and targetSum == 0:
                return True
            return self.dfs(node.left, targetSum) or self.dfs(node.right, targetSum)
        return False

    def solve(self, root, acc, targetSum):
        if not root:
            return False
        acc += root.val
        if not root.left and not root.right:
            if acc == targetSum:
                return True
        return self.solve(root.left, acc, targetSum) or self.solve(root.right, acc, targetSum)
        
    def make_tree(self, root, idx):

        rootNode = TreeNode(root[idx])
        if 2*idx+1 < len(root): rootNode.left = self.make_tree(root, 2*idx+1)
        if 2*idx+2 < len(root): rootNode.right = self.make_tree(root, 2*idx+2)
        return rootNode

print(Solution().hasPathSum([5,4,8,11,None,13,4,7,2,None,None,None,1], 22))
print(Solution().hasPathSum([1,2,3], 5))
print(Solution().hasPathSum([], 0))
