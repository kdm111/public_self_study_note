class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
'''
LeetCode 701 :  Insert into a Binary Search Tree
새로운 노드를 트리에 추가할 때 이진 탐색 트리를 유지하면서 넣어라

# sol1 153ms 14% 17MB 43% 
root의 값과 비교하면서 val이 크다면 오른쪽으로 작다면 왼쪽으로 옮긴다.

'''
from typing import Optional
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # sol1
        if not root:
            return TreeNode(val)
        if root.val < val:
            root.right = self.insertIntoBST(root.right, val)
        else:
            root.left = self.insertIntoBST(root.left, val)
        return root
