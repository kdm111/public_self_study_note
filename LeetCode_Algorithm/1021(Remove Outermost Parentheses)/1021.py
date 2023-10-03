'''
# 가장 바깥에 존재하는 괄호 없애기
# sol1 42ms 81% 16.1MB 99%
O(n) O(1)

'''

class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        # sol
        cnt = 0; ans = ""; l = 0
        for r in range(len(s)):
            if s[r] == '(':
                cnt += 1;
            else:
                cnt -= 1
            if cnt == 0:
                ans += s[l+1: r]
                l = r+1
        return ans
print(Solution().removeOuterParentheses("(()())(())"))
print(Solution().removeOuterParentheses("(()())(())(()(()))"))
