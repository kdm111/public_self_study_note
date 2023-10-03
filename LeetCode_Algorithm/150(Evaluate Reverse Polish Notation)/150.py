'''
LeetCode 150 : 

# sol1 67ms 64% 14.3MB 44%
작은 양의 정수 // 큰 음수 = -1
해결한 방법 int(작은 양의 정수 / 큰 음수)
'''
class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        for token in tokens:
            if token.isdigit() or token[1:].isdigit():
                stack.append(int(token))
            else:
                num2 = stack.pop()
                num1 = stack.pop()
                # print(num1, token, num2, self.cal(num1, token, num2))
                stack.append(self.cal(num1, token, num2))
        return stack[-1]
        
    def cal(self, num1, operator, num2):
        if operator == '+':
            return num1 + num2
        elif operator == '-':
            return num1 - num2
        elif operator == '*':
            return num1 * num2
        elif operator == '/':
            return int(num1 / num2)

# print(Solution().evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
print(Solution().evalRPN(["4","-2","/","2","-3","-","-"]))

