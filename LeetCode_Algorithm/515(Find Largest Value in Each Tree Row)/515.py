class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
'''
LeetCode 515 : Find Largest Value in Each Tree Row
각 depth에서 가장 큰 수를 구하라

# sol1 44ms 89% 16.3MB 61%
bfs로 순회하며 가장 큰 값을 저장
'''
from typing import Optional
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> list[int]:
        if not root:
            return []
        from collections import deque
        queue = deque([root])
        ans = []
        while queue:
            l = len(queue); val = queue[0].val
            for _ in range(l):
                node = queue.popleft()
                val = max(val, node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans.append(val)
        return ans
        