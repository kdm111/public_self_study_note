class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional
from collections import deque

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        headNode = makeTree(head, 0)
        # sol1 O(n), O(n) 1376~1391ms 16~15%
        # ans = []
        # q = deque()
        # q.append(headNode)
        # while q:
        #     node = q.popleft()    
        #     ans.append(node.val)
        #     if node.next:
        #         q.append(node.next)
        # for i in range(len(ans)//2):
        #     if ans[i] != ans[len(ans)-i-1]:
        #         return False
        # return True
        ## return ans == ans[::-1]

        # sol2 two pointer O(n), O(1) 924~1019 70~56
        # 처음 절반을 구한 뒤 
        # 그 절반과 그 나머지를 뒤집어서 비교
        first_half = self.end_of_first_half(headNode)
        second_half_start = self.reverse_list(first_half.next)

        first_position = headNode
        second_position = second_half_start
        while second_position is not None:
            if first_position.val != second_position.val:
                return False
            first_position = first_position.next
            second_position = second_position.next

        first_half.next= self.reverse_list(second_half_start) # 리스트를 다시 원상 복구하는 코드
        return True


    # slow는 하나 전진 fast는 두 개씩 전진    
    def end_of_first_half(self, node):
        fast = node
        slow = node
        while fast.next is not None and fast.next.next is not None:

            fast = fast.next.next
            slow = slow.next

        return slow
    # 링크드 리스트 뒤집기
    def reverse_list(self, node):
        prev = None
        curr = node
        while curr is not None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev


def makeTree(head, idx):
    headNode = ListNode(head[idx])
    if (idx+1 < len(head)):
        headNode.next = makeTree(head, idx+1)
    return headNode

print(Solution().isPalindrome([1,2,3,2,1]))