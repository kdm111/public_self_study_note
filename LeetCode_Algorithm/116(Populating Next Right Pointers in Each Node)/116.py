class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

from typing import Optional
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        # sol1 69ms 89%
        # O(n) O(n)
        # from collections import deque
        # queue = deque([root])
        # while queue:
        #     temp = []
        #     for idx in range(len(queue)):
        #         node = queue[idx]
        #         if not node:
        #             return root
        #         if idx+1 < len(queue):
        #             next_node = queue[idx+1]
        #         else:
        #             next_node = None
        #         node.next=  next_node
        #         temp.extend([node.left, node.right])
        #     queue = temp


        # sol2 149ms 15%
        # 트리를 순회할 때
        # 바로 왼쪽에 있는 자식은 오른쪽 자식을 next로 가진다.
        # 이 생각을 기반으로 알고리즘을 작성할 수 있다.
        # O(n) O(1)
        if not root:
            return root
        # leftmost는 항상 트리의 가장 왼쪽을 가진다.
        leftmost = root
        while leftmost.left:
            # left
            head = leftmost
            while head:
                # 부모의 왼쪽 자식은 부모의 오른쪽 자식을 next로 가진다.
                head.left.next = head.right
                # 부모의 형제 노드가 있을 경우 
                # 부모의 오른쪽 자식은 형제의 왼쪽 자식을 갖는다.
                if head.next:
                    head.right.next = head.next.left
                # 형제들을 옮겨 다니며 자식들의 next를 구한다.
                head = head.next
            # 가장 왼쪽노드로 이동
            leftmost = leftmost.left
        return root
    
            



print(Solution().connect)