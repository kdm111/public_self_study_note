from typing import Optional
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> list[str]:
        # 34ms 73% 14MB 23%
        self.ans = []
        self.solve(root, "")
        return self.ans
    def solve(self, node, temp):
        if not node:
            return ;
        temp = temp + f"{node.val}"
        if not node.left and not node.right:
            self.ans.append(temp)
            return ;
        self.solve(node.left, temp + "->")
        self.solve(node.right, temp + "->")

        