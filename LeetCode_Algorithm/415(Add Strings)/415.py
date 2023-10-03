class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        # sol1 59~70ms 55~38%
        # return str(int(num1)+int(num2))

        # sol2 57~61ms 59~45%
        n1 = n2 = 0
        for i in num1:
            n1 = n1*10 + ord(i) - ord('0')
        for i in num2:
            n2 = n2*10 + ord(i) - ord('0')
        return str(n1+n2)

        sol3  

print(Solution().addStrings("11", "123"))

