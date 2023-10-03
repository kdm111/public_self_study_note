from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        # sol 253ms 5%
        # O(mn)
        # 새로운 트리를 만들어 새로운 루트 노드를 반환
        # dummy.next = self.solve(root1, root2)
        # return dummy.next


        # sol2 171ms 31%
        # O(m) O(m) 트리 하나만 순회
        # 여기서는 root1을 기준으로 순회
        root1= self.solve2(root1, root2)
        return root1


    # def solve(self, root1, root2):
    #     if not root1 and not root2:
    #         return None;
    #     if not root1:
    #         root1 = TreeNode(0)
    #     if not root2:
    #         root2 = TreeNode(0)
    #     root = TreeNode(root1.val+root2.val)
    #     root.left = self.solve(root1.left, root2.left)
    #     root.right = self.solve(root1.right, root2.right)
    #     return root

    def solve2(self, root1, root2):
        if not root1:
            return root2
        if not root2:
            return root1
        root1.val += root2.val
        root1.left = self.solve2(root1.left, root2.left)
        root1.right = self.solve2(root1.right, root2.right)
        return root1
