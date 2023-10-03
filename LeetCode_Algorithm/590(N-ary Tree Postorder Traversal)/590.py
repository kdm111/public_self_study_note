class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def postorder(self, root: 'Node') -> list[int]:
        # sol1 53ms 58% 16.2MB 41%
        self.ans = []
        self.solve(root)
        return self.ans
    def solve(self, node):
        if not node:
            return 
        for child in node.children:
            self.solve(child)
        self.ans.append(node.val)
