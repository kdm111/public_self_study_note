class Solution:
    def isUgly(self, n: int) -> bool:
        # sol1 39ms 83%
        # 한 숫자로 나누어 나누기가 0이 되기 전까지 계속 나눔 
        if n < 1:
            return False
        for k in [2,3,5]:
            while n % k == 0:
                n //= k
        if n == 1:
            return True            
        return False