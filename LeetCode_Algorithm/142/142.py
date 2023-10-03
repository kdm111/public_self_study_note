from typing import Optional
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode], pos) -> Optional[ListNode]:
        # O(n) 48ms 96%
        if head == None: return head
        rootNode = self.makeTree(head, 0, pos, None)
        curr_node = rootNode
        next_node = rootNode
        while next_node and next_node.next:
            curr_node = curr_node.next
            next_node = next_node.next.next
            if curr_node == next_node: 
                break
        else: 
            return None
        while rootNode != curr_node:
            rootNode = rootNode.next
            curr_node = curr_node.next
        return rootNode


    def makeTree(self, head, idx, pos, cycle):
        rootNode = ListNode(head[idx])
        if idx == pos:
            cycle = rootNode
        if idx == len(head)-1:
            rootNode.next = cycle
        elif idx < len(head)-1:
            rootNode.next = self.makeTree(head, idx+1, pos, cycle)
        return rootNode

print(Solution().detectCycle([3,2,0,-4], 1))
print(Solution().detectCycle([1], -1))
