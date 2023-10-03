'''
LeetCode 714 : Best Time to Buy and Sell Stock with Transaction Fee

# sol1
hold는 현재 가지고 있는 주식이다. 
hold는 가장 작은 값을 
free에서 주식을 팔았을 때 얻을 수 있는 값이다.

전체 hold는 구매한것을 가정한 뒤 free는 기존 주식을 처분하고 남은 계산이다.


'''
class Solution:
    def maxProfit(self, prices: list[int], fee: int) -> int:
        # sol1 844ms 51% 21.6MB 43%
        n = len(prices)
        hold, free = [0] * n, [0] * n
        hold[0] = -prices[0]
        for i in range(1, n):
            hold[i] = max(hold[i - 1], free[i - 1] - prices[i])
            free[i] = max(free[i - 1], hold[i - 1] + prices[i] - fee)
        return free[-1]
        

print(Solution().maxProfit([1,3,2,8,4,9], 2))
print(Solution().maxProfit([9,8,7,1], 2))
