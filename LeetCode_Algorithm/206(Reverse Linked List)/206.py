from typing import List, Optional

from numpy import true_divide

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # sol1 O(n), O(1) 36~73ms 91~10%
        root = self.makeTree(head,0)     

        if head is None:
            return head

        
        curr = head.next
        prev = head
        prev.next = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev


    def makeTree(self, head, idx):
         rootNode = ListNode(head[idx])
         if (idx+1 < len(head)): rootNode.next = self.makeTree(head, idx+1)
         return rootNode



print(Solution().reverseList([1,2,3,4,5]))