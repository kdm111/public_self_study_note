# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional
class Solution:
    def makeTree(self, lst, idx):
        if idx >= len(lst):
            return None
        root = TreeNode(lst[idx])
        root.left = self.makeTree(lst,2*idx+1)
        root.right = self.makeTree(lst,2*idx+2)
        return root

    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left = cur_depth = ans = 0
        import collections 
        queue = collections.deque()
        # bfs로 queue에 node depth, pos값을 넣어줌
        queue.append((root, 0, 0))
        while queue:
            node, depth, pos = queue.popleft()
            if not node:
                continue
            # left의 경우 
            queue.append((node.left, depth+1, 2*pos))
            queue.append((node.right, depth+1, 2*pos+1))
            # depth가 달라지면 가장 최근 depth로 업데이트 하고 
            # left를 가장 작은 값으로 업데이트
            if cur_depth != depth:
                cur_depth = depth; left = pos
            # left값과 right값을 빼고 난 뒤 1을 더한다.
            ans = max(ans, pos-left+1)
        return ans

root = Solution().makeTree([1,3,2,5,None,None,9,6,None,7], 0)
# root = Solution().makeTree([1,3,2,5,3,None,9], 0)
# root = Solution().makeTree([1,3,2,5], 0)

print(Solution().widthOfBinaryTree(root))
