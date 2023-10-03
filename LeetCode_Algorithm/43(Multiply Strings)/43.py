from tkinter import N


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # sol1 51ms 70%
        # return str(int(num1) * int(num2))

        # sol2 not overflow 52ms 69%
        # n1 = 0
        # for char in num1:
        #     n1 *= 10
        #     n1 += int(char)
        # n2 = 0
        # for char in num2:
        #     n2 *= 10
        #     n2 += int(char)
        # n = n1 * n2
        # if n == 0:
        #     return "0"
        # ans = ""
        # while n > 0:
        #     ans += str(n % 10)
        #     n //= 10
        # return "".join(reversed(ans))


        # sol3 O(mn), O(m+n) 207ms 30%
        if num1 == '0' or num2 == '0': return '0'
        ans = [0] * (len(num1) + len(num2))
        num1 = num1[::-1]
        num2 = num2[::-1]

        for pos2, n2 in enumerate(num2):
            for pos1, n1 in enumerate(num1):
                    carry = ans[pos1 + pos2]
                    num = int(n1) * int(n2) + carry
                    ans[pos1 + pos2] = num % 10
                    ans[pos1 + pos2 + 1] += num // 10

        if ans[-1] == 0:
            ans.pop()
        return "".join(list(map(str, reversed(ans))))
       

print(Solution().multiply("19", "19"))