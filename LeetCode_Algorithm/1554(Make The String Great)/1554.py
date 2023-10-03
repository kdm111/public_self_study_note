'''
LeetCode 1554 : Make The String Great
대문자와 소문자가 만나는 경우 제거하라

# sol1 26ms 98% 13.9MB 54%

'''
class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for c in s:
            if stack:
                if 65 <= ord(stack[-1]) <= 90 and ord(stack[-1]) == ord(c) - 32:
                    stack.pop()
                elif 97 <= ord(stack[-1]) <= 122 and ord(stack[-1]) == ord(c) + 32:
                    stack.pop()
                else:
                    stack.append(c)
            else:
                stack.append(c)
        return "".join(stack)