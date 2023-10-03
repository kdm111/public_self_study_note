class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

'''

# sol1 O(n) O(1)
39ms 97% 16.3MB 56%

'''
from typing import Optional
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        ans = less = ListNode(-1); temp = greater = ListNode(-1); i = 0
        while head:
            if head.val < x:
                less.next = head; less = less.next; 
                head = head.next; less.next = None
            else:
                greater.next = head; greater = greater.next;
                head = head.next; greater.next = None
        less.next = temp.next
        return ans.next