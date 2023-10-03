# 

class Solution:
    def numTilings(self, n: int) -> int:
        # sol1 39ms 85% 16.1MB 97%
        dp = [0,1,2,5] + [0] * (n - 3)
        for i in range(4, n+1):
            dp[i] = (2 * dp[i-1]  + dp[i-3]) % 1000000007
        return dp[n]
        
print(Solution().numTilings(30))