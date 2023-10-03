class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import List, Optional

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
#        return self.solve1(nums, 0, len(nums)-1)
        return self.solve3(nums, 0, len(nums)-1)


    def solve1(self, nums, left, right):
        # 항상 왼쪽 노드를 루트로 잡음
        # 
        if left > right:
            return None
        idx = left + (right-left)//2
        print(left, idx, right, nums[idx])
        root = TreeNode(nums[idx])
        root.left = self.solve1(nums, left, idx-1)
        root.right = self.solve1(nums, idx+1, right)
        return root
        
    def solve2(self, nums, left, right):
        # 항상 오른쪽 노드를 루트로 잡음
        if left > right:
            return None
        idx = left + (right-left)//2
        if (left+right) % 2 == 1:
            idx += 1
        print(left, idx, right, nums[idx])
        root = TreeNode(nums[idx])
        root.left = self.solve2(nums, left, idx-1)
        root.right = self.solve2(nums, idx+1, right)
        return root

    def solve3(self, nums, left, right):
        from random import randint
        # 144ms 26%
        # 항상 어느쪽 루트를 잡을 지 랜덤으로 정함
        if left > right:
            return None
        idx = left + (right-left)//2
        if 0 < (left+right) % 2:
            idx += randint(0, 1)
        print(left, idx, right, nums[idx])
        root = TreeNode(nums[idx])
        root.left = self.solve3(nums, left, idx-1)
        root.right = self.solve3(nums, idx+1, right)
        return root

print(Solution().sortedArrayToBST([-10,-3,0,5,9]))
print(Solution().sortedArrayToBST([1,2,3,4,5,6,7,8]))
