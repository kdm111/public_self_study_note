class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional, List

class Solution:
    def makeListNode(self, arr, idx):
        if len(arr) <= idx:
            return None
        root = ListNode(arr[idx])
        root.next = self.makeListNode(arr, idx+1)
        return root

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # sol1 brute force
        # O(nlogn) O(n) 117ms 87% 
        # root = ListNode(None)
        # ans = root
        # temp = []
        # for node in lists:
        #     while node:
        #         temp.append(node)
        #         node = node.next
        # temp.sort(key= lambda x : x.val)
        # while temp:
        #     root.next = temp.pop(0)
        #     root = root.next
        # return ans.next

        # sol2 O(kn) O(1) time exceeded
        # k가 만약 n이라면 O(n^2)
        import sys
        root = ListNode(None)
        ans = root
        # 전체 깊이 카운트 세기
        cnt = 0
        for node in lists:
            while node:
                node = node.next
                cnt += 1
        while cnt > 0:
            min_node = ListNode(sys.maxsize); min_node_idx = sys.maxsize
            for idx, node in enumerate(lists):
                if node and min_node.val > node.val:
                    min_node = node; min_node_idx = idx
            root.next = min_node
            root = root.next
            min_node = min_node.next
            lists[min_node_idx] = min_node
            cnt -= 1
        return ans.next

root1 = Solution().makeListNode([1,4,5], 0)
root2 = Solution().makeListNode([1,3,4], 0)
root3 = Solution().makeListNode([2,6], 0)

print(Solution().mergeKLists([root1, root2, root3]))