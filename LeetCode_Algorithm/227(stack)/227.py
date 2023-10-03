class Solution:
    def calculate(self, s: str) -> int:
        # sol1 O(n) O(n) 363ms 5%
        # 먼저 십의 자리 숫자를 정수형으로 바꾼다.
        stack = []; temp = -1
        for idx in range(len(s)):
            # 공백 제거
            if s[idx] == ' ':
                continue;
            elif s[idx] == '*' or s[idx] == '/' or s[idx] == '+' or s[idx] == '-':
                if temp >= 0:
                    stack.append(temp); temp = -1
                stack.append(s[idx])
            elif s[idx].isdigit():
                if temp < 0: temp  = 0
                temp = (10 * temp) + int(s[idx])
        if temp >= 0:
            stack.append(temp)
        # 이제 곱셈과 나눗셈을 계산한다.
        stack2 = []
        for idx in range(len(stack)):
            if stack2 and stack2[-1] == '*':
                stack2.pop()
                stack2.append(stack2.pop() * stack[idx])
            elif stack2 and stack2[-1] == '/':
                stack2.pop()
                stack2.append(stack2.pop() // stack[idx])
            else:
                stack2.append(stack[idx])
        # 이제 덧셈과 뺄셈을 계산한다.
        ans = []
        for idx in range(len(stack2)):
            if ans and ans[-1] == '+':
                ans.pop()
                ans.append(ans.pop()+stack2[idx])
            elif ans and ans[-1] == '-':
                ans.pop()
                ans.append(ans.pop()-stack2[idx])
            else:
                ans.append(stack2[idx])
        return ans[0]

            

                
print(Solution().calculate("1*2-3/4+5*6-7*8+9/10"))
# print(Solution().calculate(" 3*5 / 2"))
# print(Solution().calculate(" 3*3+5 / 2"))
# print(Solution().calculate(" 33+53"))

