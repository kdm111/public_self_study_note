# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional

def makeTree(head, idx):
    rootNode = ListNode(head[idx])
    if idx+1 < len(head): rootNode.next = makeTree(head, idx+1)
    return rootNode

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        rootNode = makeTree(head, 0)
        # # sol1 O(n), O(1)  36~52ms 73~27% 
        # slow = rootNode
        # fast = rootNode
        # if slow.next is None: return slow.val

        # while fast is not None and fast.next is not None:
        #     slow = slow.next
        #     # if fast is not None and fast.next is not None:
        #     #     fast = fast.next.next
        #     # elif fast is not None:
        #     #     fast = fast.next

        #     # 어차피 루프를 돌기 위해서는 next가 존재해야 한다고 했으므로
        #     fast = fast.next.next

        # return slow.val


        # sol2 O(n), O(n)
        arr = [rootNode]
        while arr[-1].next:
            arr.append(arr[-1].next)
        return arr[len(arr)//2].val



            

        



print(Solution().middleNode([1,2,3,4]))