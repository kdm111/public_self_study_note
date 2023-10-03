from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # sol1 52ms 24%
        if len(root) == 0: return []
        rootNode = self.makeTree(root, 0)
        # sol1 recursive
        # ans = []
        # self.preOrder(rootNode, ans)

        # sol2 iterative
        ans = []
        nodes = [rootNode]
        while nodes:
            node = nodes.pop()
            if node.val:
                ans.append(node.val)
            if node.right:
                nodes.append(node.right)
            if node.left:
                nodes.append(node.left)
        return ans

    def makeTree(self, root, idx):
        node = TreeNode(root[idx])
        if 2 * idx + 1 < len(root): node.left = self.makeTree(root, 2*idx+1)
        if 2 * idx + 2 < len(root): node.right = self.makeTree(root, 2*idx+2)
        return node

    def preOrder(self, root, ans):
        if root.val:
            ans.append(root.val)
        if root.left:
            self.preOrder(root.left, ans)
        if root.right:
            self.preOrder(root.right, ans)

        

print(Solution().preorderTraversal([1,2,3,4,5]))