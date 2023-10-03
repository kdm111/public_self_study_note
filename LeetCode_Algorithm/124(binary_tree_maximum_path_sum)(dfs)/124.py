# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional

class Solution:

    def makeTree(self, arr, idx):
        if idx >= len(arr):
            return None
        rootnode = TreeNode(arr[idx])
        rootnode.left = self.makeTree(arr, 2*idx+1)
        rootnode.right = self.makeTree(arr, 2*idx+2)
        return rootnode

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # O(n) O(h) : h는 tree height
        import sys
        self.ans = -sys.maxsize
        self.getGain(root)
        return self.ans

    def getGain(self, root):
        if not root:
            return 0
        # 왼쪽부터 확인
        left_gain = max(self.getGain(root.left), 0)
        # 오른쪽 노드 확인
        right_gain = max(self.getGain(root.right), 0)
        # 각 노드의 최대합을 취함
        gain = left_gain + root.val + right_gain
        if self.ans < gain:
            self.ans = gain
        return root.val + max(left_gain, right_gain)

root = Solution().makeTree([-10,9,20,None,None,15,7], 0)
# root = Solution().makeTree([1,2,3], 0)
print(Solution().maxPathSum(root))