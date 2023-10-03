class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional, List
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # sol1 411ms 5% 91.12MB 17%
        # while postorder and postorder[-1] not in inorder:
        #     postorder.pop()
        # if postorder:
        #     root = TreeNode(postorder.pop())
        #     idx = inorder.index(root.val)
        #     root.left = self.buildTree(inorder[:idx], postorder[:])
        #     root.right = self.buildTree(inorder[idx+1:], postorder[:])
        #     return root

        # sol2 139ms 60% 55.61MB 52% O(n^2) O(n^2)
        # if not inorder or not postorder:
        #     return None
        # root = TreeNode(postorder.pop())
        # idx = inorder.index(root.val) # O(n)
        # root.right = self.buildTree(inorder[idx+1:], postorder) # O(n), O(n)
        # root.left = self.buildTree(inorder[:idx], postorder) # O(n), O(n)
        # return root
    
        # sol3 68ms 87% 21.02MB 87%
        # 위의 방법은 재귀에 따른 추가 공간과 inorder인덱스에서 추가 O(n)이 필요하다.
        # index의 O(n)을 없애기 위해 dict를 사용한다.
        map_inorder = {}
        for i, val in enumerate(inorder):
            map_inorder[val] = i
        # 해당 인덱스가 없다면 리턴 None
        def solve(l, r):
            if l > r: return None
            node = TreeNode(postorder.pop())
            m = map_inorder[node.val]
            node.right = solve(m+1, r)
            node.left = solve(l, m-1)
            return node
        return solve(0, len(postorder)-1)

        

root = Solution().buildTree( [9,3,15,20,7], [9,15,7,20,3])
arr = [root]
while arr:
    temp = []
    for node in arr:
        if node:
            print(node.val, end=" ")
            if node.left:
                temp.append(node.left)
            if node.right:
                temp.append(node.right)
    print()
    arr = temp[:]

