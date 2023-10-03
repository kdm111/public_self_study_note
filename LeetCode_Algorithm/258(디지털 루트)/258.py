class Solution:
    def addDigits(self, num: int) -> int:

        # sol1 55~70ms 32~7%
        num = str(num)
        while len(num) != 1:
            ans = 0
            for i in num:
                ans += int(i)
            num = str(ans)
        return num

        # sol2 
        # digital root
        


print(Solution().addDigits(38))