
'''
LeetCode 32 : Longest Valid Parentheses
주어진 문자열에서 적합한 괄호의 가장 큰 길이를 구하라

# sol1 39ms 94% 14.7MB 43%
O(n) O(n)
인덱스를 스택에 넣어서 구한다.
스택의 탑을 -1로 구현해 놓고
'('일 경우 그 인덱스를 스택에 저장하고
')' 일 경우 '('의 최근 인덱스를 제거한 뒤 
stack의 탑의 값과 현재 인덱스의 차를 저장한다.


'''
class Solution:
    def longestValidParentheses(self, s: str) -> int:

        # sol1
        stack = [-1]; ans = 0
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                ans = max(ans, i - stack[-1])
        return ans
                
'''
()()()
((()))

'''
print(Solution().longestValidParentheses("()()()"))
print(Solution().longestValidParentheses("((()))"))
print(Solution().longestValidParentheses("())())"))
print(Solution().longestValidParentheses(")()())"))
print(Solution().longestValidParentheses("()(()"))


