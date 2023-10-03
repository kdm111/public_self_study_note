from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # sol1 merge sort 977ms 44%
        if not head or not head.next:
            return head
        # 먼저 절반 노드에 해당하는 지점을 구함
        prev, left, right = None, head, head
        while right and right.next:
            prev = left
            left = left.next; right = right.next.next
        prev.next = None
        return self.merge(self.sortList(head), self.sortList(left))
    

    def merge(self, left, right):
        h = node = ListNode(None)
        while left and right:
            if left.val > right.val:
                node.next = right; right = right.next
            else:
                node.next = left; left = left.next
            node = node.next
        if left:
            node.next = left
        if right:
            node.next = right
        return h.next

    def makeTree(self, head, idx):
        root = ListNode(head[idx])
        if idx+1 < len(head): root.next = self.makeTree(head, idx+1)
        return root

head = Solution().makeTree([4,1,2,3], 0)
print(Solution().sortList(head))