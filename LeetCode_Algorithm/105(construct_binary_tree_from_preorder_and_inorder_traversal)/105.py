# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import List, Optional
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # O(n) O(n) 220ms 51%
        if inorder:
            # preorder의 첫번째는 항상 루트이다.
            idx = inorder.index(preorder.pop(0))
            root = TreeNode(inorder[idx])
            # inorder에서 루트의 왼쪽에 있는 요소는 왼쪽 트리에 해당하고 나머지는 오른쪽에 위치한다.
            # preorder에서 항상 왼쪽 노드를 향해 나아가면서 루트를 만들어 나감
            root.left = self.buildTree(preorder, inorder[:idx])
            root.right = self.buildTree(preorder, inorder[idx+1:])
            return root
        pass


print(Solution().buildTree([3,9,20,15,7], [9,3,15,20,7]))