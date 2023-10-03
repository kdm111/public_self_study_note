
from typing import List
'''
LeetCode 121 : Best Time to Buy and Sell Stock

# sol2 932ms 93% 25MB 80%
최소의 가격을 찾으면서
최소 이상의 가격이 나올 때마다 이익을 계산하여 최대 이익을 구한다.


'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # sol 1 brute force O^2 시간초과
        # ans = 0
        # for buy_day in range(len(prices)):
        #     max_sell = 0
        #     for sell_day in range(buy_day+1, len(prices)):
        #         if prices[sell_day] > max_sell: max_sell = prices[sell_day]
        #     curr_max = max_sell-prices[buy_day]
        #     if ans < curr_max: ans = curr_max
        # return ans

        # sol 2 O(n) 1080ms 34%보다 더 빠른 결과
        ans = 0
        buy_price = float("inf")
        for price in prices:
            if buy_price > price: 
                buy_price = price
            else:
                profit = price - buy_price
                if profit > ans: 
                    ans = profit
        return ans 

        


        



                    

print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))
