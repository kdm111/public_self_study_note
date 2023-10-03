'''
LeetCode 700 : Search in a Binary Search Tree
이진 탐색 트리에서 타겟 노드를 찾기

# sol1
preorder, inorder, postorder

# sol2 61ms 99% 16.5MB 57%
BST이므로 값을 찾아 이동
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional

class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        self.val = val
        # sol1 84ms 26% 16.6MB 13%
        # return self.preorder(root)

        # sol2 89ms 8% 16.3MB 95%
        # return self.inorder(root)
    
        # sol3 86ms 17% 16.5MB 57%
        return self.postorder(root)


    def preorder(self, node):
        if not node:
            return None
        if node.val == self.val:
            return node
        return self.preorder(node.left) or self.preorder(node.right)

    def inorder(self, node):
        if not node:
            return None
        left = self.inorder(node.left)
        if node.val == self.val:
            return node
        right = self.inorder(node.right)
        return left or right

    def postorder(self, node):
        if not node:
            return None
        left = self.postorder(node.left)
        right = self.postorder(node.right)
        if node.val == self.val:
            return node
        return left or right
    
    def solve(self, node):
        if not node:
            return None
        if node.val == self.val:
            return node
        else:
            if node.val < self.val:
                return self.solve(node.right)
            else:
                return self.solve(node.left)

        



