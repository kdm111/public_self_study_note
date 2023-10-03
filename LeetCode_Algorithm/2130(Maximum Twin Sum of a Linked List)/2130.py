class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
'''
LeetCode 2130 : Maximum Twin Sum of a Linked List
짝수 개의 노드로 이루어진 링크드 리스트에서 페어 (1,n)번째 (2, n-1)번째의 합이 가장 큰 수를 구하라

# sol1 883ms 88% 45MB 65%
중간 지점까지 도달한 뒤 중간 지점부터 끝까지 리버스 한 뒤 그 값을 순회하며 저장
'''
from typing import Optional
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # sol1
        # fast = slow = head
        # while fast and fast.next:
        #     slow = slow.next
        #     fast = fast.next.next
        # prev = None
        # curr = slow
        # while curr:
        #     next_node = curr.next
        #     curr.next = prev
        #     prev = curr
        #     curr = next_node
        # ans = 0
        # while prev:
        #     ans = max(ans, head.val+prev.val)
        #     prev = prev.next
        #     head = head.next
        # return ans

        # 901ms 63% 47.62MB 57%
        fast = slow = head
        prev = slow
        # 중간 지점 찾기
        while fast and fast.next:
            fast = fast.next.next
            prev = slow
            slow = slow.next
        prev.next = None
        curr = None
        while slow:
            temp = slow.next
            slow.next = curr
            curr = slow
            slow = temp
        ans = 0
        while head:
            ans = max(ans, head.val + curr+val)
            curr = curr.next
            head = head.next
        return ans        

            


        

        while head:
            head = head.next
        return 0

            
            

'''
[47,22,81,46,94,95,90,22,55,91,6,83,49,65,10,32,41,26,83,99,14,85,42,99,89,69,30,92,32,74,9,81,5,9]
47, 9

'''