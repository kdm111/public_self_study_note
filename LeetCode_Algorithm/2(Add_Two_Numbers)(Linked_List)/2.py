# Definition for singly-linked list.
from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # sol1 102~119 37~21%
        # l1 = self.makeListNode(l1, 0)
        # l2 = self.makeListNode(l2, 0)
    #     ans = self.getAns(l1, l2, 0)
    #     temp  = ans
    #     while temp:
    #         print(temp.val)
    #         temp = temp.next
    #     return ans

    # def getAns(self, l1, l2, carry):
    #     ans = ListNode()
    #     temp = l1.val + l2.val + carry
    #     carry = int(temp / 10)
    #     temp = int(temp % 10)
    #     ans.val = temp
    #     if carry >= 1 or l1.next or l2.next:
    #         l1 = ListNode() if l1.next == None else l1.next
    #         l2 = ListNode() if l2.next == None else l2.next
    #         ans.next = self.getAns(l1, l2, carry)
    #     return ans

        # sol2 78~98ms 68~42%
        l1 = self.makeListNode(l1, 0)
        l2 = self.makeListNode(l2, 0)
        ans = ListNode(0)
        ans_copy = ans
        carry = 0
        while l1 or l2 or carry:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            carry, mod = divmod(l1_val + l2_val + carry, 10) 
            ans_copy.next = ListNode(mod)
            ans_copy = ans_copy.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return ans.next


    def makeListNode(self, lst, idx):
        ret = ListNode()
        ret.val = lst[idx]
        if idx + 1 < len(lst):
            ret.next = self.makeListNode(lst, idx + 1)
        return ret
            

print(Solution().addTwoNumbers([9,9], [9]))