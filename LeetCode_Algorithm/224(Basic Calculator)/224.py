class Solution:
    def calculate(self, s: str) -> int:
        # sol1 138ms 27% 18MB 26%
        stack = []
        temp = []
        for c in s:
            if c == ' ':
                continue
            elif c == ')':
                while stack and stack[-1] != '(':
                    a = stack.pop()
                    temp.append(a)
                stack.pop(); temp = temp[::-1]
                stack.append(self.cal(temp))
            elif c.isdigit():
                if stack and isinstance(stack[-1], int): 
                    n = stack.pop()
                    stack.append(10 * n + int(c))
                else:
                    stack.append(int(c))
            else:
                stack.append(c)
        return self.cal(stack)

    def cal(self, stack):
        if isinstance(stack[0], int):
            ret = stack[0]; stack.pop(0)
        else:
            stack.pop(0)
            n = stack.pop(0)
            ret = -n
        while stack:
            m = stack.pop(0)
            if m == '+':
                n = stack.pop(0)
                ret += n
            elif m == '-':
                if stack:
                    n = stack.pop(0)
                    ret -= n
                else:
                    return -1 * ret
        return ret
                

print(Solution().calculate("1-(     -2)"))
print(Solution().calculate("1-(-2)"))
print(Solution().calculate("-1-2+3"))



