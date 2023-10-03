class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # sol1 O(logn), O(1) 36~56ms 81~27%

        # if n==0: return False
        # if n==1: return True
        # while n != 1:
        #     if n % 2 != 0: break
        #     n //= 2

        # return True if n == 1 or n == 2 else False
        # if n==0: return False

        # while n % 2 == 0:
        #     n /= 2

        # return n==1
        
        # sol2 O(1), O(1) 37~40ms 73~67%
        # 컴퓨터는 음수를 2의 보수로 표현한다.
        # 숫자의 모든 비트에 not을 취한 다음 +1하여 표현한다.

        #  7 0000 0111
        # -7 1111 1001
        # 2의 지수가 아닌 음수와 양수의 & 연산은 rightmost bit에 1을 남긴다.
        # 7 & -7 0000 0001
        #  8 0000 1000
        # -8 1111 1000
        # 2의 지수인 음수와 양수의 & 연산은 양수를 나타낸다.
        # 따라서 
        # if n==0: return False
        # return ((n) & (-n) == n)

        # sol3 O(1), O(1)
        # 4비트 에서 
        # 2의 제곱인 수는 -1이 되었을 경우
        # 1000
        # 0111
        # 위와 같이 나온다.
        # 따라서 두 수를 & 연산하면 0이 된다.
        if n==0: return False
        return n & (n-1) == 0






print(Solution().isPowerOfTwo(4))