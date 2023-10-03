class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
'''
leet 1161 : 

# sol1 294ms 85% 20.9MB 79%
각 레벨의 합을 구한 뒤 커지는 순간 level을 체크함
'''
from typing import Optional

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        # sol1
        queue = [root]; level = 1
        total = root.val; ans = level
        while queue:
            temp = 0
            queueTemp = []
            for node in queue:
                temp += node.val
                if node.left: queueTemp.append(node.left)
                if node.right: queueTemp.append(node.right)
            if total < temp:
                total = temp; ans = level
            queue = queueTemp[:]
            level += 1
        return ans
        
