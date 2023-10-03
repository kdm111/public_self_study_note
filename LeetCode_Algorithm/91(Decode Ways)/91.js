var numDecodings = function(s) {
  // sol1 55ms 99% 42.1MB 88%
  let dp = new Array(s.length+1).fill(0)
  dp[0] = 1
  if (s[0] != '0') { dp[1] = 1 }
  for (let i = 2; i <= s.length; i++) {
    if (s[i-1] != '0') {
      dp[i] = dp[i-1]
    }
    let n = parseInt(s.slice(i-2, i))
    if (n >= 10 && n <= 26) {
      dp[i] += dp[i-2]
    }
  }
  return dp[s.length]
};

console.log(numDecodings("12"))