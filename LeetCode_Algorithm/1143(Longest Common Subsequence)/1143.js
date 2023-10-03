var longestCommonSubsequence = function(text1, text2) {
  // sol3 83ms 94% 72.37MB 73%
  let dp = Array.from(Array(text2.length + 1), () => {return Array(text1.length + 1).fill(0)})
  for (let i = 0; i < text2.length; i++) {
    for (let j = 0; j < text1.length; j++) {
      dp[i+1][j+1] = (text1[j] === text2[i]) ? dp[i][j] + 1 : Math.max(dp[i][j+1], dp[i+1][j])
    }  
  }
  return dp[dp.length-1][dp[0].length-1]
};

console.log(longestCommonSubsequence("abcde", "ace"))