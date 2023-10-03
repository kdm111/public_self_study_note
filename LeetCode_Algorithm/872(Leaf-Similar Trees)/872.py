'''
LeetCode 872 : Leaf-Similar Trees
두 트리가 주어질 때 리프가 같은 지 확인

# sol1 33ms 94% 13.9MB 87%
O(n) O(n)
preorder로 순회 후 확인

'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        root1Leaf = []; root2Leaf = []
        self.traversal(root1, root1Leaf)
        self.traversal(root2, root2Leaf)
        if len(root1Leaf) != len(root2Leaf):
            return False
        for i in range(len(root1Leaf)):
            if root1Leaf[i] != root2Leaf[i]:
                return False
        return True
            
    def traversal(self, node, arr):
        if not node:
            return ;
        if not node.left and not node.right:
            arr.append(node.val)
        self.traversal(node.left, arr)
        self.traversal(node.right, arr)

        
        