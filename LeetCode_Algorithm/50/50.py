class Solution:
    def myPow(self, x: float, n: int) -> float:
        # 44ms 45%
        # return pow(x,n)
        
        # 49ms 32%
        # return x ** n

        # O(n) time exceeded
        # if n < 0:
        #     x = 1 / x
        #     n = -n
        # ans = 1
        # while n > 0:
        #     ans *= x;
        #     n -= 1
        # return ans

        # O(logn) 62ms 10%
        def fastPow(x, n):
            if n == 0:
                return 1.0
            half = fastPow(x, n // 2)
            if n % 2 == 0:
                return half * half
            else:
                return half * half * x
            
        if n < 0:
            x = 1 / x; n = -n
        return fastPow(x, n)


print(Solution().myPow(2.000, -2))