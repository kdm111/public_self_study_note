from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        return list(bin(n)[2:])


print(Solution().countBits(2))