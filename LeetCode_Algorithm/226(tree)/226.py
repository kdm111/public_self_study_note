# Definition for a binary tree node.
from logging import root
from turtle import left
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from collections import deque

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if len(root) == 0: return []
        # sol1 O(n), O(h) 32~47ms 88~43%
        # recursive 
        # h는 트리의 높이
        rootNode = self.makeTree(root, 0)
        self.invert(rootNode)

        q = deque()
        q.append(rootNode)
        while q:
            node=q.popleft()
            print(node.val, end=" ")
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
        return rootNode
        

    def invert(self, rootNode):
        noneNode = TreeNode(None)
        if rootNode is None: return
        rootNode.left, rootNode.right = rootNode.right , rootNode.left
        self.invert(rootNode.left)
        self.invert(rootNode.right)
        # elif rootNode.left and rootNode.right is None: 
            
        #     rootNode.left, rootNode.right = None, rootNode.left
        #     self.invert(rootNode.right)
        # elif rootNode.right and rootNode.left is None: 
        #     rootNode.left, rootNode.right = rootNode.right, None
        #     self.invert(rootNode.left)





    def makeTree(self, root, idx):
        rootNode = TreeNode(root[idx])
        if 2*idx+1 < len(root): rootNode.left = self.makeTree(root, 2*idx+1)
        if 2*idx+2 < len(root): rootNode.right = self.makeTree(root, 2*idx+2)
        return rootNode


print(Solution().invertTree([1,2]))