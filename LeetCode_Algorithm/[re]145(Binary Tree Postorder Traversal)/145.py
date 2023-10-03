class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional, List
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # sol1 65ms 11%
        # recur O(n) O(n)
        # self.ans = []
        # self.dfs(root)
        # return self.ans


        # sol2 35ms 87%
        # iter O(n) O(n)
        # from collections import deque
        # stack = deque([root])
        # ans = []
        # while stack:
        #     node = stack.pop()
        #     if node:
        #         ans.append(node.val)
        #         stack.append(node.left)
        #         stack.append(node.right)
        # return ans[::-1]

        # sol3
        # Morris Traversal
        # 여기에서는 preorder의 결과를 뒤집는 것으로 구현

        # ans = []
        # curr = root
        # while curr:
        #     if not curr.left:
        #         ans.append(curr.val)
        #         curr = curr.right
        #     else:
        #         prev = curr.left
        #         while prev and prev.right != curr:
        #             prev = prev.right
        #         if prev.right == None:
        #             ans.append(curr.val)
        #             prev.right = curr
        #             curr = curr.left
        #         else:
        #             prev.right = None
        #             curr = curr.right
        # return ans                
                
            
        
    def dfs(self, node):
        if node:
            self.dfs(node.left)
            self.dfs(node.right)
            self.ans.append(node.val)

