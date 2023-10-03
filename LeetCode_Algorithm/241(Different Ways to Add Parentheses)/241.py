from typing import List
from unittest import expectedFailure
class Solution:
    def __init__(self):
        self.memo = {}
    def diffWaysToCompute(self, expression: str) -> List[int]:
        # sol1 55ms 61%
        if expression.isdigit():
            return [int(expression)]
        # memo를 사용함으로써 똑같은 계산 하는 것을 줄임
        if expression in self.memo:
            return self.memo[expression]
        ans = []
        for i,c in enumerate(expression):
            if c in "+-*":
                left = self.diffWaysToCompute(expression[:i])
                right = self.diffWaysToCompute(expression[i+1:])
                for j in left:
                    for k in right:
                        ans.append(self.cal(j,c,k))
        self.memo[expression] = ans
        return ans
    def cal(self, m, op, n):
        if op == '+':
            return m+n
        elif op == '-':
            return m-n
        else:
            return m*n
        
print(Solution().diffWaysToCompute("2-1-4"))
# print(Solution().diffWaysToCompute("2-1-1"))
# print(Solution().diffWaysToCompute("2*3-4*5"))

