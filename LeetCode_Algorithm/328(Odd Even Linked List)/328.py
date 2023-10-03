'''
LeetCode 328 : Odd Even Linked List
싱글 링크드 리스트가 존재할 때 홀수번째 노드와 짝수번째 노드 순서대로 정렬하라.
'''
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head = self.makeTree(head, 0)
        # sol1 O(n) O(n) 59ms 66%
        # 임의의 두 개의 노드를 만들어 순서대로 넣은 뒤 출력
        odd = ListNode(None); even = ListNode(None)
        oddhead = odd; evenhead = even
        c = 1
        while head:
            if c % 2:
                odd.next = head
                odd = odd.next
            else:
                even.next = head
                even = even.next
            c += 1
            head = head.next
        even.next = None
        odd.next = evenhead.next
        return oddhead.next
    
        # sol2 58ms 67% 18.82MB 92%
        # 노드에서 진행시키면서 
        if not head or not head.next:
            return head

        odd = head
        even = middle = head.next
        
        while (odd and odd.next) and (even and even.next):
            temp = odd.next.next
            temp2 = even.next.next
            odd.next = temp
            even.next = temp2
            odd = odd.next
            even = even.next
        if even:
            even.next = None
        odd.next = middle
        return head


    def makeTree(self, head, idx):
        root = ListNode(head[idx])
        if idx+1 < len(head): root.next = self.makeTree(head, idx+1)
        return root

print(Solution().oddEvenList([1,2,3,4,5]))