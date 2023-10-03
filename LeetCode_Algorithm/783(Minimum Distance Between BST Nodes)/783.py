# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
'''
LeetCode 783 : Minimum Distance Between BST Nodes
두 노드사이의 가장 작은 차이를 구하라

# sol1 26ms 96% 13.8MB 74%
inorder로 순회 하면서 현재 노드 값을 이전 값으로 저장한다.
재귀로 순회하며 이전 값에서 현재 노드값을 뺀 뒤 값을 저장한다.
'''
from typing import Optional
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        ans = float("inf"); pre = -1
        def solve(node):
            nonlocal pre, ans
            if not node:
                return ;
            solve(node.left)
            if pre >= 0:
                ans = min(ans, abs(pre - node.val))
            pre = node.val
            solve(node.right)
        solve(root)
        return ans


        
        
        