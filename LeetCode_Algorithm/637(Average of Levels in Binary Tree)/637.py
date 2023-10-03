class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import List, Optional
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        # sol1 54ms 92%
        # bfs
        if not root:
            return []
        from collections import deque
        queue = deque([root])
        ans = []
        while queue:
            temp = []; node_sum = 0
            for node in queue:
                node_sum += node.val
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            ans.append(node_sum/len(queue))
            queue = temp
        return ans



