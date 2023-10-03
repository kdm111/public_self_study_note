var findBall = function(grid) {
  // 1
  // var ans = [...Array(grid[0].length).keys()]
  // 2
  var ans = Array.from(Array(grid[0].length).keys())

  // sol1 95ms 67%
  for (let c in grid[0]) {
    for (let r in grid) {
      let temp = grid[r][ans[c]]
      ans[c] += grid[r][ans[c]]
      if (ans[c] < 0 || ans[c] >= grid[0].length) {
        ans[c] = -1; break
      }
      if (temp != grid[r][ans[c]]) {
        ans[c] = -1; break
      }
    }
  }
  return ans
};


console.log(findBall([[1,1,1,-1,-1],[1,1,1,-1,-1],[-1,-1,-1,1,1],[1,1,1,1,-1],[-1,-1,-1,-1,-1]]))