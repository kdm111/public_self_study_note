# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from email import header
import tarfile
from typing import Optional
class Solution:
    def makeLinkedList(self, nodes, idx):
        if idx >= len(nodes):
            return None
        root = ListNode(nodes[idx])
        root.next = self.makeLinkedList(nodes, idx+1)
        return root

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # 87ms 33%
        cnt = 0; node = head
        while node and cnt < k:
            node = node.next
            cnt += 1
        if cnt < k: return head
        new_head, prev = self.reverseLinkedList(head, cnt)
        head.next = self.reverseKGroup(new_head, k)
        return prev

    def reverseLinkedList(self, head, cnt):
        prev, curr, next = None, head, head
        while cnt > 0:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
            cnt -= 1
        return (curr, prev)

    def print(self, root):
        while root:
            print(root.val)
            root = root.next
        return
        
root = Solution().makeLinkedList([1,2,3,4,5], 0)
root = Solution().reverseKGroup(root, 2)
Solution().print(root)
