class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
'''
LeetCode 270 : Closest Binary Search Tree Value
트리 노드에서 타겟에 가장 가까운 값을 찾아라

# sol1 53ms 18% 16.1MB 74%
bfs로 순회하여 답 도출 

# sol2


'''
from typing import Optional
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        # sol1
        ans = 0
        abs_val = float("inf")
        from collections import deque
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if abs(node.val - target) < abs_val:
                abs_val = abs(node.val - target)
                ans = node.val
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return ans

        
                
