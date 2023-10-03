class Solution:
    def decodeString(self, s: str) -> str:
        # sol1 stack 35ms 81%
        # stack = []
        # for c in s:
        #     if c == ']':
        #         string = ""
        #         while stack and not stack[-1].isdigit():
        #             temp = stack.pop()
        #             if temp.isalpha():
        #                 string += temp
        #         num = ""
        #         while stack and stack[-1].isdigit():
        #             temp = stack.pop()
        #             if temp.isdigit():
        #                 num += temp
        #         num = int("".join(num[::-1])) if num != "" else 1
        #         while num > 0:
        #             for c in "".join(reversed(string)):
        #                 stack.append(c)
        #             num -= 1
        #     else:
        #         stack.append(c)
        #   return "".join(stack)

        # sol2 31ms 99% 16.1MB 96%
        stack = []
        for c in s:
            if c == ']':
                temp = ""
                while stack[-1] != '[':
                    temp += stack.pop()
                stack.pop()
                num = ""
                while stack and '0' <= stack[-1] <= '9':
                    num += stack.pop()
                for _ in range(int(num[::-1])):
                    stack.append(temp)
            else:
                stack.append(c)
        ans = ""
        while stack:
            ans += stack.pop(0)[::-1]
        return ans
                                     

print(Solution().decodeString("10[a]"))
print(Solution().decodeString("3[a]2[bc]"))
print(Solution().decodeString("3[a2[c]]"))
print(Solution().decodeString("3[2[c]]"))

