class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
'''
LeetCode 530 : Minimum Absolute Difference in BST
두 노드의 차이가 최소인 절대값을 구하라
[334,277,507,null,285,null,678]
[0,null,2236,1277,2776,519]

# sol1 64ms 30% 16.3MB 18%
bfs로 순회하며 모든 밸류를 저장한 뒤 소트 후 미니멈 값 찾기

# sol2 67ms 19% 16.2MB 18%
주어진 트리는 이진 탐색 트리이므로 트리를 순회하므로 
정렬된 밸류 배열을 만들 수 있다.

# sol3 53ms 85% 16.2MB 33%
inorder로 순회하여 리스트를 만든다.

'''
from typing import Optional

class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        # sol1
        # from collections import deque
        # queue = deque([root]); ans = float("inf")
        # val = []
        # while queue:
        #     node = queue.popleft()
        #     if not node:
        #         continue
        #     val.append(node.val)
        #     queue.append(node.left); queue.append(node.right)
        # val.sort()
        # for i in range(len(val)-1, 0, -1):
        #     ans = min(ans, val[i] - val[i-1])
        # return ans
    
        # sol2
        # ans = float("inf")
        # val = self.solve(root)
        # for i in range(len(val)-1, 0, -1):
        #     ans = min(ans, val[i] - val[i-1])
        # return ans

        # sol3
        values = []
        stack = []; curr = root
        while stack or curr:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                curr = stack.pop()
                values.append(curr.val)
                curr = curr.right
        ans = float("inf")
        for i in range(len(values)-1, 0, -1):
            ans = min(ans, values[i]-values[i-1])
        return ans
    def solve(self, node):
        if not node:
            return []
        left = self.solve(node.left)
        right = self.solve(node.right)
        left.append(node.val)
        return left + right

