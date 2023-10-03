# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
'''
LeetCode 222 : Count Complete Tree Nodes
주어지는 완전 2진 트리의 노드 숫자를 세기

sol1 445ms 5% 21.4MB 46%
O(n) O(n)
트리를 레벨 오더 순회하면서 노드를 하나씩 체크함

sol2 161ms 41% 21.4MB 87%
O(log^2n) O(1)
위의 솔루션은 너무 성적이 좋지 않다
이미 문제에서는 주어지는 트리가 완전 2진트리라는 설명을 했다.
이를 통해 시간을 줄일 수 있을 까?

일단 depth를 구해야 한다.
root에서 left 노드만 따라가서 최대 뎁스를 구할 수 있다.

각 레벨에서 가질 수 있는 노드의 수는 2**level개가 된다.
또한 트리가 가질 수 있는 최대 노드 수는 2**depth-1개가 된다.
최대 노드 개수에서 

'''
from typing import Optional
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        # sol1
        # ans = 0; stack = [root]
        # while stack:
        #     node = stack.pop(0)
        #     if node:
        #         ans += 1
        #         stack.extend([node.left, node.right])
        # return ans

        # sol2
        if not root:
            return 0
        depth = self.findDepth(root)
        if depth == 0:
            return 1
        left, right = 1, 2 ** depth-1
        while left <= right:
            mid = left + (right-left) // 2
            # 현재 깊이에 
            if self.exist(mid, depth, root):
                left = mid+1
            else:
                right = mid-1
        print(left)
        return 2 ** depth - 1 + left

    def exist(self, mid, depth, node):
        left, right = 0, 2**depth-1
        for _ in range(depth):
            pivot = left + (right-left) // 2
            # 가질 수 있는 mid보다 현재 pivot이 더 클 경우
            if mid <= pivot:
                node = node.left; right = pivot
            else:
                node = node.right; left = pivot+1
        return node != None
            
    def findDepth(self, root):
        ret = 0
        while root.left:
            ret += 1
            root = root.left
        return ret