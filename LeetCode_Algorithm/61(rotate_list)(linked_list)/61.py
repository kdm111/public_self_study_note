# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional

class Solution:
    def makeListNode(self, lst, idx):
        if idx >= len(lst):
            return None
        root = ListNode(lst[idx])
        root.next = self.makeListNode(lst,idx+1)
        return root
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # sol1
        # 2000000000 maximum recursion
        # if k == 0 or head is None or head.next is None:
        #     return head
        # dummy = ListNode(None)
        # dummy.next= head
        
        # while head.next and head.next.next:
        #     head = head.next
        # prev = head
        # next = head.next
        # prev.next = None
        # next.next = dummy.next
        # return self.rotateRight(next, k-1)

        # sol2 O(N) O(1) 124ms 5%
        if k == 0 or head is None or head.next is None:
            return head
        dummy = head
        cnt = 0
        # 전체 깊이를 계산한 뒤 
        while dummy:
            dummy = dummy.next
            cnt += 1
        cnt = k % cnt
        while cnt > 0:
            dummy = ListNode(None)
            dummy.next = head
            while head.next and head.next.next:
                head = head.next
            prev = head; next = head.next;
            prev.next = None; next.next = dummy.next
            head = next
            cnt -= 1
        return head.val

root = Solution().makeListNode([1,2,3,4,5], 0)
print(Solution().rotateRight(root, 2))

