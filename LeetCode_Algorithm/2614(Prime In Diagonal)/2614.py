# time limit exceeded
primeTable = [0] * (4*(10 ** 6) + 1)
primeTable[0] = -1; primeTable[1] = -1
for i in range(2, 4*(10 ** 6) + 1):
    for j in range(2, i):
        if primeTable[j] == 0 and i % j == 0:
            primeTable[i] = -1
        break 


class Solution:
    def diagonalPrime(self, nums: list[list[int]]) -> int:
        # sol1 783ms 60% 28.3MB 99%
        i = 0; j = len(nums[0])-1; ans = 0
        while i < len(nums[0]):
            ans = max(self.isPrime(nums[i][i]), ans, self.isPrime(nums[j][i]))
            i += 1; j -= 1
        return ans

    def isPrime(self, n):
        i = 2
        while i * i <= n:
            if n % i == 0:
                return -1
            i += 1
        return n if n >= 2 else -1