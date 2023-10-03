class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional
from collections import deque

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        rootNode = makeTree(root, 0)
        # preorderTraversal(rootNode)
        

        # sol1 340ms 50%정도 
        # leetcode에서는 tree의 루트 노드만 주기 때문에 순회만 구현하면 됨
        # q = deque()
        # q.append(rootNode)
        # ans = 0
        # while q:
        #     node = q.popleft()
        #     if node.val is not None and low <= node.val <= high:
        #         ans += node.val
        #     if node.left: q.append(node.left)
        #     if node.right: q.append(node.right)
        # return ans
        
        # sol2 250ms 80%보다 빠름
        # 문제는 이진탐색 트리 이므로 현재 노드 값이 
        # subtree 안에서 왼쪽 자식 트리는 항상 현재 노드보다 작다.
        # subtree 안에서 오른쪽 자식 트리는 항상 현재 노드보다 크다.
        from collections import deque
        q = deque([root])
        ans = 0
        while q:
            node = q.popleft()
            if low <= node.val <= high:
                ans += node.val
            if low < node.val and node.left:
                q.append(node.left)
            if node.val < high and node.right:
                q.append(node.right)
        return ans

            

def makeTree(root, idx):
    if len(root) == 0: return
    if idx > len(root)-1: return
    
    rootNode = TreeNode(root[idx])
    if 2*idx+1 < len(root):
        rootNode.left = makeTree(root, 2*idx+1)
    if 2*idx+2 < len(root):
        rootNode.right = makeTree(root, 2*idx+2)
    return rootNode 

def preorderTraversal(node):
    if node is None: return

    print(node.val, end=" ")
    preorderTraversal(node.left)
    preorderTraversal(node.right)
    

    


print(Solution().rangeSumBST([10,5,15,3,7,13,18,1,None,6], 6, 10))
