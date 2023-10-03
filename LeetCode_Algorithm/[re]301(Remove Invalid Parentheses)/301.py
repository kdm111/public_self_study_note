from typing import List
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        for i in range(len(s)):
            
                
                
    def isValid(self, s):
        cnt = 0
        for c in s:
            if c == '(':
                cnt += 1
            else:
                cnt -= 1
            if cnt < 0:
                return False
        return cnt == 0

        pass

print(Solution().removeInvalidParentheses("()())()"))