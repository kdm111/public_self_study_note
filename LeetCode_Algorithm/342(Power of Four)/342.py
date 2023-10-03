
from cmath import log


class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        # sol1 sol 63ms 20%
        # while n >= 4:
        #     n, k = divmod(n, 4)
        #     if k:
        #         return False
        # return True if n == 1 else False
        
        # sol2 log 사용
        # 40ms 79%
        # return n > 0 and log(n, 4).is_integer()

        pass            
         
        

print(Solution().isPowerOfFour(3))