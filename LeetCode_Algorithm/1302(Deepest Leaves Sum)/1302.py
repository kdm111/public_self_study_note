class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
'''
LeetCode 1302 : Deepest Leaves Sum
가장 깊은 뎁스의 리프 노드의 합을 구하라

# sol1 202ms 82% 17.8MB 64%
bfs로 돌면서 가장 마지막 리프값 합을 구한다.

'''
from typing import Optional
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        from collections import deque
        queue = deque([root])
        while queue:
            ans = 0
            l = len(queue)
            for _ in range(l):
                node = queue.popleft()
                ans += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return ans
