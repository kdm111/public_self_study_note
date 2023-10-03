class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # sol1 56ms 63% 16.4MB 19%
        if not head or not head.next:
            return head
        ans = prev = ListNode(-1); curr = head; nxt = head.next
        while nxt:
            if curr.val != nxt.val:
                prev.next = curr
                prev = curr
                curr = nxt
                nxt = nxt.next
            else:
                while nxt and curr.val == nxt.val:
                    nxt = nxt.next
                prev.next = nxt
                prev = prev.next
                curr = nxt
                nxt = nxt.next
        return ans.next
                
                
                    
                
            prev.next = curr
            prev = prev.next
            curr = curr.next
        prev.next = curr
        return head
            
        pass

