
from string import ascii_lowercase
class Solution:
    def removeDuplicates(self, s: str) -> str:
        # sol1 O(n), O(n-d) 
        # d는 duplicate의 숫자
        # 88~139ms 78~33%

        # stack = []
        # for c in s:
        #     if len(stack) == 0:
        #         stack.append(c)
        #     elif stack[-1] == c:
        #         stack.pop()
        #     else:
        #         stack.append(c)

        # return "".join(stack)

        # sol2 O(n^2), O(n) 시간초과

        duplicates = [2*c for c in ascii_lowercase]

        prev_length = -1
        while prev_length != len(s): # 중복 제거 이전과 현재 길이가 같다면 그만
            prev_length = len(s) # 중복 제거 이전 문자열 길이 저장
            for d in duplicates:
                s = s.replace(d, "") # 중복 제거
        return s

print(Solution().removeDuplicates("abbaca"))