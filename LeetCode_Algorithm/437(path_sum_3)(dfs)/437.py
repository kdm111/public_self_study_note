
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        root = self.makeTree(root, 0)
        # O(n^2), O(1) 665ms 31% 17.7MB 71%
        # 모든 패스의 합이 타겟이 되는 길의 개수를 찾는 문제
        # dfs를 두번 돌려서 해결한다.
        # preorder로 트리를 순회하되 각각의 노드부터 findPath를 통해서 
        def solve(root, targetSum):
            if root is None or root.val is None:
                return 
            findPath(root, targetSum)
            # preorder
            solve(root.left, targetSum)
            solve(root.right, targetSum)
        # 들어온 노드부터 시작하여 가능한 길을 찾아냄
        def findPath(root, targetSum):
            if root is None or root.val is None:
                return 
            if root.val == targetSum:
               self.ans += 1
            findPath(root.left, targetSum-root.val)
            findPath(root.right, targetSum-root.val)

        self.ans = 0
        if root is None: return 0
        solve(root, targetSum)
        return self.ans
  
    def makeTree(self, root, idx):
        if idx >= len(root):
            return None
        rootNode = TreeNode(root[idx])
        rootNode.left = self.makeTree(root, 2*idx+1)
        rootNode.right = self.makeTree(root, 2*idx+2)
        return rootNode

# print(Solution().pathSum([10,5,-3,3,2,None,11,3,-2,None,1], 8))
print(Solution().pathSum([1,None,2,None,3,None,4,None,5], 3))
# print(Solution().pathSum([0,1,1], 1))
# print(Solution().pathSum([5,4,8,11,None,13,4,7,2,None,5,1], 22))
