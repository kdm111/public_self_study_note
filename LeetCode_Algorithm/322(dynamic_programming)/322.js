var coinChange = function(coins, amount) {
  // sol1 O(n) O(n) 191ms 46%
  let dp = new Array(amount+1).fill(amount+1)
  dp[0] = 0

  for (let idx=0; idx <= amount;idx++) {
    for (let coin of coins) {
      if (idx > coin || coin ==idx) {
        dp[idx] = Math.min(dp[idx], dp[idx-coin]+1)
      }
    }
  }
  if (dp[amount] != amount+1){
    return dp[amount]
  } else {
    return -1
  }

};

console.log(coinChange([1,2,5], 11))
console.log(coinChange([2], 3))
