class Solution:
    def myAtoi(self, s: str) -> int:
        # 52ms 42%
        idx = 0
        while idx < len(s) and s[idx] == ' ':
            idx += 1
        plus = 0
        minus = 0
        while idx < len(s) and (s[idx] == '+' or s[idx] == '-'):
            if s[idx] == '+':
                plus += 1
            if s[idx] == '-':
                minus += 1
            idx += 1
        if (plus and minus) or (2 <= plus) or (2 <= minus):
            return 0
        ans = 0
        while idx < len(s) and '0' <= s[idx] <= '9':
            if ans <= -214748375:
                return -2147483648
            if 214748365 <= ans:
                return 2147483647
            ans *= 10
            ans += int(s[idx])
            idx += 1
        if minus:
            ans *= -1
        if -2 ** 31 <= ans <= 2 ** 31 -1:
            return ans
        if ans < -2 * 31:
            return -2147483648
        if 2 ** 31 <= ans:
            return 2147483647
        return 0
        
print(Solution().myAtoi("42"))
