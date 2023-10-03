from numpy import integer


class Solution:
    def reverse(self, x: int) -> int:
        # 72ms 5%
        temp = str(x)
        ans = 0
        for char in temp[::-1]:
            if char == '-':
                ans *= -1
            else:
                ans *= 10
                ans += int(char)
        if -2 ** 31 <= ans <= 2**31 -1:
            return ans
        else:
            return 0




print(Solution().reverse(1534236469))