var wordBreak = function(s, wordDict) {
  // sol1 72ms 82% 43.5MB 74%
  let dp = new Array(s.length+1).fill(false)
  dp[0] = true
  for (let i = 0; i < s.length; i++) {
    for (let j = i+1; j < s.length+1; j++) {
      if (dp[i] && wordDict.indexOf(s.slice(i, j)) >= 0)
        dp[j] = true
    }
  }
  return dp[s.length]
};