class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        rootNode = self.makeTree(root, 0)
        # O(n) O(1) 145ms 17% iterative
        # while rootNode:
        #     rootnode_val = rootNode.val
        #     if p > rootnode_val and q > rootnode_val:
        #         rootNode = rootNode.right
        #     elif p < rootnode_val and q < rootnode_val:
        #         rootNode = rootNode.left
        #     else:
        #         return rootNode

        # sol2 O(n) O(n)(재귀 스택) recursive 89ms 76%
        return self.solve(rootNode, p, q)
    def solve(self, root, p, q):
        if p > root.val and q > root.val:
            return self.solve(root.right, p, q)
        elif p < root.val and q < root.val:
            return self.solve(root.left, p, q)
        else:
            return root.val

    def makeTree(self, root, idx):
        rootNode = TreeNode(root[idx])
        if 2*idx+1 < len(root): rootNode.left = self.makeTree(root, 2*idx+1)
        if 2*idx+2 < len(root): rootNode.right = self.makeTree(root, 2*idx+2)
        return rootNode



print(Solution().lowestCommonAncestor([6,2,8,0,4,7,9,None,None,3,5], 2,8))