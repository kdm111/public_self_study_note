class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
'''
LeetCode 1448 : Count Good Nodes in Binary Tree
루트에서 시작하여 현재 path동안 가장 큰 수보다 더 큰 수를 가지고 있거나 같은 수를 가지고 있으면 good node라고 한다.
트리에서 good node의 수를 구하라.

# sol1 255ms 72% 32.5Mb 37%
현재 path를 돌면서 가장 큰 수를 저장한다.
현재 노드의 값이 더 크거나 같다면 수를 업데이트하고 
순회를 계속한다.
'''
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        if not root:
            return 0
        self.ans = 0
        self.solve(root, root.val)
        return self.ans
    def solve(self, node, node_val):
        if not node:
            return ;

        if node_val <= node.val:
            node_val = node.val
            self.ans += 1
        self.solve(node.left, node_val)
        self.solve(node.right, node_val)
