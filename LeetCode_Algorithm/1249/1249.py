
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # sol1 O(n) 1397ms 10%
        # p = []
        # idx_array = []
        # for idx, char in enumerate(s):
        #     if char == '(':
        #         p.append(char)
        #         idx_array.append(idx) 
        #     elif char == ')':
        #         if len(p) != 0 and p[-1] == '(':
        #             p.pop()
        #             idx_array.pop()
        #         else:
        #             idx_array.append(idx)
        #             p.append(char)
        # ans = ""
        # for idx, char in enumerate(s):
        #     if idx in idx_array:
        #         continue
        #     else:
        #         ans += char
        # return ans

        # sol2 764ms 14%
        s = list(s)
        stack = []
        for idx in range(len(s)):
            if s[idx] == '(':
                stack.append(idx)
            elif s[idx] == ')':
                if len(stack) == 0:
                    s[idx] = ''
                else:
                    stack.pop()
        for i in range(len(s)):
            if i in stack:
                s[i] = ''
        return ''.join(s)

                    



print(Solution().minRemoveToMakeValid("a)b(c)d"))