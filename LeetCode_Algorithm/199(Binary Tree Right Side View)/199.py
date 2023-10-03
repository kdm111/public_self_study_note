'''
LeetCode 199 : Binary Tree Right Side View
이진 트리를 오른쪽에서 봤을 때 루트에서 부터 순서대로 리턴하라.

# sol2 39ms 37% 13.9MB 16%
bfs로 순회하면서 만나는 노드의 가장 끝의 노드의 값을 저장해서 리턴한다.
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional, List
class Solution:
    def makeTree(self, lst, idx):
        if idx >= len(lst):
            return None
        root = TreeNode(lst[idx])
        root.left = self.makeTree(lst, 2*idx+1)
        root.right = self.makeTree(lst, 2*idx+2)
        return root

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # sol1 O(n) O(n) 44ms 68% 
        # level order 
        # if root == None: return []
        # ans = []
        # stack = [[root]]
        # while stack:
        #     nodes = stack.pop(0)
        #     if nodes == []:
        #         break
        #     temp = []
        #     for node in nodes:
        #         val = node.val
        #         if node.left:
        #             temp.append(node.left)
        #         if node.right:
        #             temp.append(node.right)
        #     ans.append(val)
        #     stack.append(temp)
        # return ans


        # sol2
        from collections import deque
        if not root:
            return []
        queue = deque([root]); ans = []
        while queue:
            l = len(queue)
            for _ in range(l):
                node = queue.popleft()
                val = node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans.append(val)
        return ans

root = Solution().makeTree([1,2,3,None,5,None,4], 0)
root = Solution().makeTree([1,2], 0)

print(Solution().rightSideView(root))