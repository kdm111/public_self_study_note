# Definition for a binary tree node.
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

    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # sol1 O(n) O(n) 55ms 39%
        # from collections import deque
        # if not root:
        #     return []
        # queue = deque()
        # queue.append(root)
        # ans = [[root.val]]
        # while queue:
        #     temp_node = []; temp_ans = []
        #     while queue:
        #         node = queue.popleft()
        #         if node and node.left:
        #             temp_node.append(node.left)
        #             temp_ans.append(node.left.val)
        #         if node and node.right:
        #             temp_node.append(node.right)
        #             temp_ans.append(node.right.val)
        #     if len(ans) % 2 == 1:
        #         temp_ans.reverse();
        #     if temp_ans != []:
        #         ans.append(temp_ans)
        #     queue.extend(temp_node)
        # return ans 

        # sol2 37ms 47% 14.2MB 47%
        if not root:
            return []
        from collections import deque
        queue = deque([root]); ans = []; depth = 0
        while queue:
            temp = []; l = len(queue)
            for _ in range(l):
                node = queue.popleft()
                temp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if depth % 2:
                temp = temp[::-1]
            depth += 1
            ans.append(temp)
        return ans
                

root = Solution().makeTree([1,2,3,4,5], 0)
print(Solution().zigzagLevelOrder(root))