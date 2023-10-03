class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
'''
LeetCode 173 : Binary Search Tree Iterator
주어진 tree를 inorder로 순회하는 BSTIterator 만들기

sol1 T : 116ms 75% S : 20.6MB 12%
T : O(n) S : O(n)
트리가 주어졌을 때 init에서 트리를 inorder로 순회한 뒤 그 순회값을 모두 저장해
하나씩 출력한다.
'''
from typing import Optional
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        from collections import deque
        self.queue = deque([])
        self.arr = deque([])
        while True:
            if root:
                self.queue.append(root)
                root = root.left
            elif self.queue:
                node = self.queue.pop()
                self.arr.append(node)
                root = node.right
            else:
                break
        
    def next(self) -> int:
        node = self.arr.popleft()
        return node.val

    def hasNext(self) -> bool:
        return True if self.arr else False