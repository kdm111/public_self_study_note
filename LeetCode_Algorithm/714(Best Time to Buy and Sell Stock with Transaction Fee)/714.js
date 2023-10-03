var maxProfit = function(prices, fee) {
  // sol1 73ms 55% 53.5MB 38%
  let hold = Array(prices.length).fill(0)
  let free = Array(fee.length).fill(0)
  hold[0] = -prices[0]
  for (let i = 1; i < prices.length; i++) {
    hold[i] = Math.max(hold[i-1], free[i-1] - prices[i])
    free[i] = Math.max(free[i-1], hold[i-1] + prices[i] - fee)
  }
  return free[free.length-1]
};