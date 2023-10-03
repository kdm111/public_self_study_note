class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
'''
leetCode 276 : 

# sol1
276ms 97% 64.16MB 53%
O(n) O(n)
dfs로 순회하면서 거리를 카운트한다.

'''
from typing import Optional
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:

        def solve(node, dir, cnt):
            if not node:
                return cnt
            if dir == 'l':
                return max(solve(node.left, 'l', 0), solve(node.right, 'r', cnt+1))
            else:
                return max(solve(node.left, 'l', cnt+1), solve(node.right, 'r', 0))
        return max(solve(root.left, 'l', 0), solve(root.right, 'r', 0))