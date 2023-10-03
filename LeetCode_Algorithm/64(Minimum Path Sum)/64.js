var minPathSum = function(grid) {
  // sol2 71ms 81% 44.6MB 44%
  let dp = Array()
  for (let i = 0; i < grid.length; i++) {
    dp.push(Array(grid[0].length).fill(0))
  }
  dp[0][0] = grid[0][0]
  for (let r=1; r < grid.length; r++) {
    dp[r][0] = grid[r][0] + dp[r-1][0]
  }
  for (let c=1; c < grid[0].length;c++) {
    dp[0][c] = grid[0][c] + dp[0][c-1]
  }
  for (let r=1; r < grid.length; r++) {
    for (let c=1; c < grid[0].length; c++) {
      dp[r][c] = grid[r][c] + Math.min(dp[r-1][c], dp[r][c-1])
    }
  }
  console.log(dp)
  return dp[grid.length-1][grid[0].length-1]
};

console.log(minPathSum([[1,3,1],[1,5,1],[4,2,1]]))