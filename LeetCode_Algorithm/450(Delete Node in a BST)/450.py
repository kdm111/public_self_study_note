class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

'''
LeetCode 450
key와 같은 node를 삭제하라.

삭제 한 뒤에 트리가 유지될 수 있도록 재구성해야 한다.
현재 
'''
from typing import Optional

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # sol1 87ms 33% 20.7MB 17%     
        if not root:
             return None
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            if not root.left and not root.right:
                root = None
            elif root.right:
                root.val = self.findval(root)
                root.right = self.deleteNode(root.right, root.val)
            else:
                root.val = self.findval2(root)
                root.left = self.deleteNode(root.left, root.val)
        return root

    def findval(self, node):
        node = node.right
        while node.left:
            node = node.left
        return node.val

    def findval2(self, node):
        node = node.left
        while node.right:
            node = node.right
        return node.val

        