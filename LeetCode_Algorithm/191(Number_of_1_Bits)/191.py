

class Solution:
    def hammingWeight(self, n: int) -> int:
        # sol1 python 29~38ms 91~66%
        # return bin(n).count('1')

        # sol2 bit mask 31~65ms 89~7%
        cnt = 0
        for mask in range(32):
            if (1 << mask) & n:
                cnt += 1
        return (cnt)

print(Solution().hammingWeight(7))