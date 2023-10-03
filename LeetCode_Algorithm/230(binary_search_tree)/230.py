class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        root = self.makeTree(root, 0)
        lst = []
        # 99ms 21%
        # 먼저 left에 대해서만 리스트에 넣는다.
        # 그리고 k를 계속 빼가면서 k가 0이 될 때까지 체크한다.

        while True:
            while root:
                lst.append(root)
                root = root.left
            k -= 1
            root = lst.pop()
            if k == 0:
                return root.val
            root = root.right
            
        
    def makeTree(self, root, idx):
        if len(root) <= idx: return None
        rootNode = TreeNode(root[idx])
        rootNode.left = self.makeTree(root, 2*idx+1)
        rootNode.right = self.makeTree(root, 2*idx+2)
        return rootNode


print(Solution().kthSmallest([3,1,4,None,2],2))