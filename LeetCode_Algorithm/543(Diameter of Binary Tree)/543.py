class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from turtle import right
from typing import Optional
from collections import deque

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # sol1 O(n) 48~85ms 85~20%보다 빠름
        # 트리의 최대 직경을 구하는 문제로 
        # postorder를 활용해야 한다.
        # left child의 뎁스와 right child 뎁스 중
        # 가장 큰 하나를 선택해서 노드로 넘겨주어야 한다.
        # 그러면 가장 큰 직경이 되는 경우만을 선택하여 계속해서 postorder로 돌면서 계산한다.

        self._diameter = 0
        rootNode = self.makeTree(root, 0)
        # treeLevelPrint(rootNode)
        self.postOrderTraversal(rootNode)
        return self._diameter

    def makeTree(self, root, idx):
        
        rootNode = TreeNode(val=root[idx])
        if 2*idx+1 < len(root): 
            rootNode.left = self.makeTree(root, 2*idx+1)
        if 2*idx+2 < len(root):
            rootNode.right =self. makeTree(root, 2*idx+2)
        return rootNode

    def postOrderTraversal(self, node):
        if node is None: return 0
        left_depth = 0
        right_depth = 0

        left_depth = self.postOrderTraversal(node.left)
        right_depth =  self.postOrderTraversal(node.right)
        # 때마다 
        self._diameter = max(self._diameter, left_depth+right_depth)

        return max(left_depth, right_depth)+1


def treeLevelPrint(node):
    if node is None: return
    q = deque()
    q.append(node)
    while 0 < len(q):
        level_cnt = len(q)
        for _ in range(level_cnt):
            curr_node = q.popleft()
            print(curr_node.val, end=" ")
            if curr_node.left:
                q.append(curr_node.left)
            if curr_node.right:
                q.append(curr_node.right)
        print(' ')

        pass

print(Solution().diameterOfBinaryTree([1,2,3,4,5]))