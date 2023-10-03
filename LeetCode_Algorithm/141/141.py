# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
from pickletools import read_uint1
from typing import Optional, List
class Solution:
    def hasCycle(self, head: Optional[ListNode], pos:int) -> bool:

        # sol1 O(n), O(1) 80~116ms 48~10%
        # Floyd's cycle finding algorithm
        if len(head)==1: return False
        rootNode = self.makeTree(head, 0)

        endNode = rootNode
        while endNode.next != None:
            endNode = endNode.next

        idx = 0
        while idx < pos:
            returnNode = rootNode.next
            idx += 1
        endNode.next = returnNode

        # currNode = rootNode
        # nextNode = rootNode.next

        # while currNode != nextNode:
        #     if nextNode == None or nextNode.next == None:
        #         return False
        #     currNode = currNode.next
        #     nextNode = nextNode.next.next
        # return True

        # sol2 O(n), O(n) 56~64ms 91~74%
        # hashTable
        # seen = set()
        # while rootNode is not None:
        #     if rootNode in seen: return True
        #     seen.add(rootNode)
        #     rootNode = rootNode.next
        # return False

        # sol3 
        slow = rootNode
        fast = rootNode
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
        
                


    def makeTree(self,head, idx):
        rootNode = ListNode(head[idx])
        if idx+1 < len(head): rootNode.next = self.makeTree(head, idx+1)
        return rootNode
  

print(Solution().hasCycle([3,2,0,-4], 1))