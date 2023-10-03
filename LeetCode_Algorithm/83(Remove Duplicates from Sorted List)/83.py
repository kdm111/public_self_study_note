# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # sol1 104ms 5%
        # O(n) O(n)
        if not head:
            return head
        self.stack = []
        curr = head
        def solve(prev, curr):
            if curr:
                if curr.val in self.stack:
                    node = curr.next
                    prev.next = node
                    solve(prev, node)
                else:
                    self.stack.append(curr.val)
                    solve(curr, curr.next)        
        solve(None, curr)
        return head

        # sol2 57ms 71%
        # O(n) O(1)
        # 리스트 노드는 정렬되어 있으므로 O(1)이 가능하다.
        if not head:
            return head
        prev= head; curr = head.next
        while curr != None:
            if prev.val == curr.val:
                curr = curr.next
                prev.next = curr
            else:
                prev = curr
                curr = curr.next
        return head

