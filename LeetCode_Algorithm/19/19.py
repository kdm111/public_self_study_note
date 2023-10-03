from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # O(n) O(1) 44ms 68%
        head = self.makeTree(head, 0)
        if n == 0: return head
        dummy = ListNode(None)
        dummy.next = head
        lenNode = dummy
        length = 0
        while lenNode.next:
            lenNode = lenNode.next
            length += 1
        first = dummy
        length -= n
        while length > 0:
            first = first.next; length -= 1
        first.next = first.next.next
        return dummy.next.val
            
            
            

        pass
    def makeTree(self, root, idx):
        rootNode = ListNode(root[idx])
        if idx+1 < len(root): rootNode.next = self.makeTree(root, idx+1)
        return rootNode


print(Solution().removeNthFromEnd([1,2,3,4,5], 1))
# print(Solution().removeNthFromEnd([1], 1))
