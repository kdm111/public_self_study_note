class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import List, Optional

from numpy import right_shift
from collections import deque

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        rootNode = self.makeTree(root, 0)

        # sol1 recursive O(n), O(n) 풀이 43~54ms 66~39%
    #     return self.checkLeftRight(rootNode, rootNode)

    # def checkLeftRight(self, left, right):
    #     if left == None and right == None: return True
    #     if left == None or right == None: return False
    #     return left.val == right.val \
    #         and self.checkLeftRight(left.left, right.right) \
    #         and self.checkLeftRight(left.right, right.left)
  

        # sol2 53~57ms 41~32%
        # iterative using deque
        q = deque()
        q.append(rootNode); q.append(rootNode) 

        while q:
            left = q.popleft()
            right = q.popleft()

            if left == None and right == None: continue
            if left == None or right == None: return False
            if left.val != right.val: return False
            q.append(left.left); q.append(right.right)
            q.append(left.right); q.append(right.left)
        return True




        # sol1  O(n), O(n) 47~71ms 56~10% 
        # left.val == right.val
        # left.left.val == right.right.val
        # left.right.val == right.left.val
        # 이런 식으로 재귀 함수를 작성하여 문제풀기
        # 
    #     left = rootNode.left
    #     right = rootNode.right
    #     if left or right:
    #         return self.checkLeftRight(left, right)
    #     else:
    #         return True

    # def checkLeftRight(self, left, right):
    #     if left and right:
    #         val = False if left.val != right.val else True
    #         if left.left or right.right:
    #             left_val = self.checkLeftRight(left.left, right.right)
    #         else:
    #             left_val = True
    #         if left.right or right.left:
    #             right_val = self.checkLeftRight(left.right, right.left)
    #         else:
    #             right_val = True
    #         return val and left_val and right_val
    #     else:
    #         return False

        

        
    # def isSymmetric(self, tree: List) -> bool:
        
        # sol1
        # 0 1 3 7 15
        # 트리 전체가 들어올 경우 
        # tree[1:1+2], tree[3:3+4], tree[7:7+8]
        # 부분부분으로 잘라서 체크할 수 있다.

        # i, j = 1, 2
        # n = 1
        # while j<len(tree):
        #     for idx in range(i, i+j):
        #         if tree[idx] != tree[j+i-idx]:
        #             return False
        #     i += 2**n
        #     j = i+2**(n+1)
        # return True
    def makeTree(self, root, idx):
        # if idx > len(root): return
        rootNode = TreeNode(root[idx])
        if 2*idx+1 < len(root): rootNode.left = self.makeTree(root, 2*idx+1)
        if 2*idx+2 < len(root): rootNode.right = self.makeTree(root, 2*idx+2)
        return rootNode
 


print(Solution().isSymmetric([1,2,2,None,3,None,3]))