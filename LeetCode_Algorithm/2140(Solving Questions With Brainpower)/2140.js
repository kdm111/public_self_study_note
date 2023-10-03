var mostPoints = function(questions) {
  // sol2 196ms 86% 76MB 97%
  let dp = new Array(questions.length + 1).fill(0)  
  let n = questions.length
  for (let i = n - 1; i > -1; i--) {
    let j = i + questions[i][1] + 1
    dp[i] = Math.max(questions[i][0] + dp[Math.min(j, n)], dp[i+1])
  }
  return dp[0]
};