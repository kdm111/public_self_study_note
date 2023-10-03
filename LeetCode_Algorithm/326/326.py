class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        # sol1 log3 147~178ms 26~15%
        while 3 <= n:
            if n % 3 == 0:
                n /= 3 
            else:
                return False
        return True if n == 1 else False

print(Solution().isPowerOfThree(0))