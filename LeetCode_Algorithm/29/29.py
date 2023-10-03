class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # 55ms 38%
        # ans = int(dividend / divisor)
        # if ans >= 2 ** 31 -1:
        #     return 2147483647
        # elif ans <= -2 ** 31:
        #     return -2147483648
        # else:
        #     return ans


        # python의 경우 32bit 이상의 overflow를 핸들링할 필요는 없지만
        # c의 경우 필요하다.
        # O(logn) 53ms 43%
        max_int = 2147483647
        min_int = -2147483648
        half_min_int = -1073741824

        if dividend == min_int and divisor == -1:
            return max_int
        negative = 1
        if dividend < 0: negative *= -1; dividend *= -1
        if divisor < 0: negative *= -1; divisor *= -1

        power_of_two = []
        doubles = []
        p = 1
        while divisor <= dividend:
            power_of_two.append(p)
            doubles.append(divisor)
            divisor += divisor
            p += p

        quotient = 0
        for i in reversed(range(len(doubles))):
            if doubles[i] <= dividend:
                quotient += power_of_two[i]
                dividend -= doubles[i]

        if negative == -1:
            return -quotient
        else:
            return quotient







        

print(Solution().divide(10,3))
print(Solution().divide(7,-3))

