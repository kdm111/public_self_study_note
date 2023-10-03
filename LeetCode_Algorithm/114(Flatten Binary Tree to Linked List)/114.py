# Definition for a binary tree node.
'''
LeetCode 114 : Flatten Binary Tree to Linked List
주어진 트리를 오른쪽으로 기울여서 담아라

# sol1 41ms 76% 15.2MB 85%
왼쪽으로 쭉 내려간 뒤 오른쪽의 서브 트리를 계속해서 내려간다.
그런 뒤 왼쪽 노드가 존재한다면 왼쪽 노드의 현재 노드의 오른쪽 트리르 부여한뒤
현재 노드의 오른쪽에 현재 노드의 왼쪽을 넣는다. 그리고 현재 노드의 왼쪽은 null로 만든다.


'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        self.solve(root)
    def solve(self, node):
        if not node:
            return None
        if not node.left and not node.right:
            return node
        left = self.solve(node.left)
        right = self.solve(node.right)
        if left:
            left.right = node.right
            node.right = node.left
            node.left = None
        return right if right else left