var numTilings = function(n) {
  // sol1 54ms 75% 43.8MB 53%
  let dp = [0,1,2,5]
  for (let i = 4; i <= n; i++ ){
    dp.push(0)
    dp[i] = (2 * dp[i-1] + dp[i-3]) % 1000000007
  }  
  return dp[n]
};