'''
LeetCode 129 : Sum Root to Leaf Numbers

# sol1 24ms 96% 13.7MB 95MB
트리를 순회하면서 leaf에 도달하게 되면 val을 더함
'''
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        self.solve(root, 0)
        return self.ans
    def solve(self, node, val):
        if not node:
            return 
        if not node.left and not node.right:
            val = val * 10 + node.val
            self.ans += val
            return 
        self.solve(node.left, val*10 + node.val)
        self.solve(node.right, val*10 + node.val)