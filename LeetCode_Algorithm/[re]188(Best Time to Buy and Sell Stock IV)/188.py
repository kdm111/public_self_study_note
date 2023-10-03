class Solution:
    def maxProfit(self, k: int, prices: list[int]) -> int:
        # sol1
        def dp(i, price, k):
            if i == len(prices) or k == 0:
                return 0
            ans = dp(i + 1, price, k)
            if price:
                ans = max(ans, prices[i] + dp(i + 1, False, k - 1))
            else:
                ans = max(ans, -prices[i] + dp(i + 1, True, k))
            return ans
        return dp(0, False, k)  
    
print(Solution().maxProfit(2, [2, 4, 1]))
print(Solution().maxProfit(2, [3,2,6,5,0,3]))
