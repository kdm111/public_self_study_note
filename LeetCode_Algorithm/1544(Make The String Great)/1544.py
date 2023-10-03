'''
LeetCode 1544 : MakeGood
주어지는 문자열을 좋게 만들어라
좋은 문자열은 두 개의 인접한 문자가 같은 글자이지만 소문자 이거나 대문자 인것이 없는 것을 말한다.

# sol1 77ms 35% 13.8MB 97%
O(n) O(n)
스택을 만들어서 스택의 top과 비교하여 해당 조건에 해당하는 지 살펴본다.
해당 조건에 맞으면 pop을 통해 없애고 문자열을 좋게 만든다.
'''
class Solution:
    def makeGood(self, s: str) -> str:
        # sol1
        stack = []
        for c in s:
            if not stack:
                stack.append(c)
            else:
                if 'a' <= c <= 'z' and stack[-1] == chr(ord(c) - 32):
                    stack.pop()
                elif 'A' <= c <= 'Z' and stack[-1] == chr(ord(c) + 32):
                    stack.pop()
                else:
                    stack.append(c)
        return "".join(stack)
print(Solution().makeGood("s"))