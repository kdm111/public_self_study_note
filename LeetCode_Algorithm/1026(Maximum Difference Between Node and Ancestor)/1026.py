class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

'''
LeetCode 1026 : Maximum Difference Between Node and Ancestor
현재 path에서 자식과 조상간의 차가 가장 큰 숫자를 구하시오

# sol1 37ms 86% 19.9MB 89%
현재 노드에서 길을 따라가면서 최대값과 최소값을 저장한다.
트리의 끝에 도달했을 시 현재까지 길에서 있었던 최대값 - 최소값의 절대값을 계산하여 리턴한다.
그 중 나타난 가장 큰 값을 리턴한다.

'''
from typing import Optional
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return self.solve(root, root.val, root.val)
    def solve(self, node, curr_max, curr_min):
        if not node:
            return abs(curr_max - curr_min)
        curr_max = max(node.val, curr_max)
        curr_min = min(node.val, curr_min)
        left = self.solve(node.left, curr_max, curr_min)
        right = self.solve(node.right, curr_max, curr_min)
        return max(left,  right)
        
