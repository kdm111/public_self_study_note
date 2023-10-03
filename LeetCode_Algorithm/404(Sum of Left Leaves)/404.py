class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

'''
LeetCode 404 Sum of Left Leaves
왼쪽 leave의 합을 구하기

sol1 62ms 52% 14.1MB 98%
T O(n) O(n)
levelorder로 돌면서 확인
그 때 노드가 만약 왼쪽에 있는 잎이라면 그 때 더한다.
'''
from typing import Optional
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        stack = [root]; ans = 0
        while stack:
            node = stack.pop()
            if node:
                if node.left is not None:
                    stack.append(node.left)
                    if node.left.left is None and node.left.right is None:
                        ans += node.left.val
                if node.right is not None:
                    stack.append(node.right)
        return ans
                
                