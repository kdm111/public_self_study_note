# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional, List
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # sol1 61ms 22%
        # recursive O(n) O(n)
        # self.ans = []
        # self.dfs(root)
        # return self.ans


        # sol2 53ms 46%
        # iterative O(n) O(n)
        # if not root:
        #     return []
        # stack = []; ans = []
        # while root != None or stack:
        #     while root != None:
        #         stack.append(root)
        #         root = root.left
        #     root = stack.pop()
        #     ans.append(root.val)
        #     root = root.right
        # return ans

        # sol3 53ms 46%
        # Morris traversal O(n) O(1)
        # 트리를 skewed하게 만들어서 O(1)을 만드는 방법
        ans = []
        while root:
            if root.left == None:
                ans.append(root.val)
                root = root.right
            else:
                prev = root.left
                # 왼쪽 서브 트리의 가장 오른쪽까지 이동한 뒤
                while prev.right != None:
                    prev = prev.right
                # root를 서브 트리의 오른쪽에 root를 연결한뒤
                prev.right = root
                # 현재 노드를 저장한 뒤
                temp = root
                # 왼쪽 서브트리의 최상단 노드로 이동
                root = root.left
                # 있었던 노드의 left는 None으로 치환
                temp.left = None
        return ans
                

            

        



    def dfs(self, node):
        if node:
            self.dfs(node.left)
            self.ans.append(node.val)
            self.dfs(node.right)
