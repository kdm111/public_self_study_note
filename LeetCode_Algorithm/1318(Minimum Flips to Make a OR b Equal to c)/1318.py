'''
LeetCode : 1318
비트 조작을 통해 a or b == c가 되도록 몇 개의 비트를 수정해야 하는가?

# sol1
비트 마스크를 통해 or 계산 결과 비교해서 비트 수를 계산
'''

class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        # sol1 30ms 94% 16.4MB 32%
        ans = 0
        while a != 0 or b != 0 or c != 0:
            x, y, z = (a & 1), (b & 1), (c & 1)
            if (x | y) != z:
                if z == 1:
                    ans += 1
                else:
                    if x != z:
                        ans += 1
                    if y != z:
                        ans += 1
            a >>= 1; b >>= 1; c >>= 1
        return ans
        
print(Solution().minFlips(2,6,5))
print(Solution().minFlips(1,2,3))
print(Solution().minFlips(4,2,7))