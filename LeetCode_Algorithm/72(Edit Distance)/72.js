var minDistance = function(word1, word2) {
  // sol1 87ms 28% 47.5MB 45%
  let dp = Array(word2.length+1).fill(0).map(
    () => {return Array(word1.length+1).fill(0)
  })
  for (let r = 0; r < word2.length+1; r++) {
    dp[r][0] = r
  }
  for (let c = 0; c < word1.length+1; c++) {
    dp[0][c] = c
  }
  for (let c = 1; c < word1.length+1; c++) {
    for (let r = 1; r < word2.length+1; r++) {
      if (word2[r-1] == word1[c-1]) {
        dp[r][c] = dp[r-1][c-1]
      } else {
        dp[r][c] = 1 + Math.min(dp[r-1][c-1], dp[r-1][c], dp[r][c-1])
      }
    }
  }
  return dp[dp.length-1][dp[0].length-1]
};

console.log(minDistance("horse", "ros"))