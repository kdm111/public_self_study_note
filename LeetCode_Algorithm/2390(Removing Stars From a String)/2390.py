'''
LeetCode 2390 : Removing Stars From a String
*가 나오면 문자열 하나를 삭제

# sol1 스택 사용
'''
class Solution:
    def removeStars(self, s: str) -> str:
        # sol1 O(n) 266ms 44%
        stack = []
        for c in s:
            if c == '*':
                if stack:
                    stack.pop()
            else:
                stack.append(c)
        return "".join(stack)