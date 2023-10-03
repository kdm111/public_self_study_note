# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional, List

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        rootNode = self.makeTree(root, 0)


        # iterative O(n) O(n) 46ms 67%
        # if not rootNode: return []
        # stack = [rootNode]
        # ans = []
        # while stack:
        #     temp = []
        #     for _ in range(len(stack)):
        #         node = stack.pop(0)
        #         temp.append(node.val)
        #         if node.left: stack.append(node.left)
        #         if node.right: stack.append(node.right)
        #     ans.append(temp)
        # return ans


        # recursive O(n) O(n) 46ms 67%
        stack = [rootNode]; temp = []; ans = []
        self.solve(stack, temp, ans)
        return ans

    def solve(self, stack, temp, ans):
        if not stack: return ;
        children = []
        while stack:
            node = stack.pop(0)
            temp.append(node.val)
            if node.left: children.append(node.left)
            if node.right: children.append(node.right)
        ans.append(temp)
        self.solve(children, [], ans)

        

    def makeTree(self, root, idx):
        if root[idx] == None: return ;
        rootNode = TreeNode(root[idx])
        if 2*idx+1 < len(root) and root[2*idx+1] != None: rootNode.left = self.makeTree(root, 2*idx+1)
        if 2*idx+2 < len(root) and root[2*idx+2] != None: rootNode.right = self.makeTree(root, 2*idx+2)
        return rootNode

# print(Solution().levelOrder([3,9,20,None,None,15,7]))
# print(Solution().levelOrder([1,2,3,4,5]))
print(Solution().levelOrder([1,2,None,3,None,4,None,5]))


    