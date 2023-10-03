# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional
from urllib.parse import ParseResultBytes

class Solution:
    def makeListNode(self, root, idx):
        if idx >= len(root):
            return None
        rootNode = ListNode(root[idx]) 
        rootNode.next = self.makeListNode(root, idx+1)
        return rootNode

    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # sol1 iterative
        # O(n) O(1) 32ms 93%
        if head is None or head.next is None:
            return head
        
        prev = ListNode(None); prev.next = head
        ans = prev
        while head and head.next:
            # 초기화
            first, second = head, head.next
            # 노드 스왑
            prev.next = second
            # first.next에 second.next에 연결
            first.next = second.next
            # second의 next의 첫번째 연결
            second.next = first
            # prev는 head의 바로 이전 노드
            prev = first
            head = first.next
        return ans.next
        
        pass

head = Solution().makeListNode([1,2,3,4], 0)
print(Solution().swapPairs(head))