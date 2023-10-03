class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional
class Solution:
    # balanced tree
    # 모든 리프노드들이 같은 레벨을 가지도록 밸런스를 맞춰주는 트리
    # 좌우의 높이를 비교하여 1 이상 차이나면 false
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        root = self.makeTree(root, 0)
        return self.solve(root)[0]
        # bottom up 69ms 71%
    def solve(self, root):
        if root is None:
            return (True, -1)
        left_balanced, left_height = self.solve(root.left)
        right_balanced, right_height = self.solve(root.right)
        if left_balanced == False or right_balanced == False:
            return (False, 0)
        return ((abs(left_height-right_height) < 2), 1+max(left_height, right_height))

    def makeTree(self, root, idx):
        rootNode = TreeNode(root[idx])
        if 2*idx+1 < len(root): rootNode.left = self.makeTree(root, 2*idx+1)
        if 2*idx+2 < len(root): rootNode.right = self.makeTree(root,2*idx+2)
        return rootNode
print(Solution().isBalanced([3,9,20,None,None,15,7]))