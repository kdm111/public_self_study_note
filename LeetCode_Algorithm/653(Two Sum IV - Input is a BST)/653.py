'''
LeetCode 653 : Two Sum IV - Input is a BST
주어지는 이진 트리에서 두 요소를 더한 값이 k가 되면 true를 반환하라.

# sol1 455ms 5% 16.6MB 73%
어떤 노드를 더해야 참이 될 지 모르므로 가능한 
모든 요소를 다 저장한 뒤 각각 노드를 방문하며
하나씩 더해본다. 맞다면 true를 반환한다.

'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional

class Solution:
    def makeTree(self, arr, i):
        root = TreeNode(arr[i])
        if 2*i + 1 < len(arr): root.left = self.makeTree(arr, 2*i+1)
        if 2*i + 2 < len(arr): root.right = self.makeTree(arr, 2*i+2)
        return root

    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        # sol1
        # arr = [root]; temp = []
        # while arr:
        #     node = arr.pop()
        #     if node:
        #         temp.append(node.val)
        #         arr.append(node.left)
        #         arr.append(node.right)

        # for i in range(len(temp)):
        #     for j in range(i, len(temp)):
        #         if temp[i] + temp[j] == k:
        #             return True
        # return False


            
            

root = Solution().makeTree([5,3,6,2,4,None,7], 0)
print(Solution().findTarget(root, 9))
# arr = [root]
# # level order
# while arr:
#     node = arr.pop(0)
#     if node and node.val:
#         print(node.val, end=" ")
#         arr.append(node.left)
#         arr.append(node.right)
# print()
# # preorder
# arr = [root]
# while arr:
#     node = arr.pop()
#     if node and node.val:
#         print(node.val, end=" ")
#         arr.append(node.right)
#         arr.append(node.left)
# print()
# # inorder
# arr = []
# node = root
# while True:
#     while node:
#         arr.append(node)
#         node = node.left
#     if arr:
#         node = arr.pop()
#         if node.val:
#             print(node.val, end=" ")
#         node = node.right
#     else:
#         break ;
# print()
# # postorder
# arr = []; node = root
# while True:
#     while node:
#         if node.right:
#             arr.append(node.right)
#         arr.append(node)
#         node = node.left
#     if arr:
#         node = arr.pop()
#         if arr and node.right and node.right == arr[-1]:
#             arr.pop()
#             arr.append(node)
#             node = node.right
#         else:
#             if node.val:
#                 print(node.val, end=" ")
#             node = None
#     else:
#         break ;