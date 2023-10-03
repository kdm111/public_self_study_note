from typing import Optional
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        # 일반 배열로 푼 문제
        # ans = []
        # list1_idx = 0
        # list2_idx = 0
        
        # while list1_idx < len(list1) and list2_idx < len(list2):
        #     if list1[list1_idx] < list2[list2_idx]:
        #         ans.append(list1[list1_idx])
        #         list1_idx += 1
        #     else:
        #         ans.append(list2[list2_idx])
        #         list2_idx += 1
        
        # while list1_idx < len(list1):
        #     ans.append(list1[list1_idx])
        #     list1_idx += 1

        # while list2_idx < len(list2):
        #     ans.append(list2[list2_idx])
        #     list2_idx += 1

        # 위의 방법으로는 풀리지 않고 리스트 노드를 활용해야 문제를 풀 수 있다. 49ms


        ans = ListNode(0)
        curr = ans

        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next

        curr.next = list1 or list2
            
        return ans.next
print(Solution().mergeTwoLists([1,2,4], [1,3,4]))

            

        