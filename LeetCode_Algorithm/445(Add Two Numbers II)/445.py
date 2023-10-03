class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
'''
링크드 리스트에 들어있는 십의 숫자를 더해 링크드 리스트로 반환

# sol1 83ms 56% 16.4MB 31%

'''
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        stack1 = self.makeStack(l1); stack2 = self.makeStack(l2)
        ans = None
        stack = []
        while stack1 or stack2:
            val = 0
            if stack1: val += stack1.pop().val
            if stack2: val += stack2.pop().val
            if ans: val += ans.val
            (a, b)= divmod(val, 10)
            stack.append(ListNode(b))
            ans = ListNode(a)
        if ans and ans.val != 0:
            stack.append(ans)
        ans = stack[-1]
        temp = ans
        for i in range(len(stack)-2, -1, -1):
            temp.next = stack[i]
            temp = stack[i]
        return ans

    def makeStack(self, l):
        stack = []
        while l:
            stack.append(l)
            l = l.next
        return stack