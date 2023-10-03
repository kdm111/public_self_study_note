from typing import List

class Solution:
    # dfs time out
    # def __init__(self):
    #     self.temp = 10002

    # def coinChange(self, coins: List[int], amount: int) -> int:
    #     if amount < 0: return -1
    #     elif amount == 0: return 0
    #     coins.sort(reverse=True)
    #     self.solve(coins, amount, 0)
    #     return self.temp if self.temp != 10002 else -1

    # def solve(self, coins, amount, ans):
    #     if amount == 0:
    #         if self.temp > ans:
    #             self.temp = ans
    #         return
    #     for coin in coins:
    #         if 1 <= coin and 0 <= amount-coin:
    #             self.solve(coins, amount-coin,ans+1)
    #         else:
    #             break

    # sol2 dp O(n*s)(각 리스트 요소를 계산하여 걸리는 시간) O(s)(dp 리스트 길이) 1649 68%
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0: return 0
        dp = [amount+1 for _ in range(amount+1)]
        dp[0] = 0
        for num in range(amount + 1):
            for coin in coins:
                if num-coin >= 0:
                    dp[num] = min(dp[num], dp[num-coin]+1)
        if dp[amount] == amount + 1:
            return -1
        return dp[amount]



print(Solution().coinChange([1,2,5],100))
print(Solution().coinChange([1,2],11))
print(Solution().coinChange([3],3))
print(Solution().coinChange([2],3))
print(Solution().coinChange([1],0))
