var maxIncreaseKeepingSkyline = function(grid) {
  // sol1 303ms 5%
  let ans = 0;
  for (let r in grid) {
    for (let c in grid) {
      let availableValue = Math.min(getRowMaxVal(grid, r,c), getColMaxVal(grid, r, c))
      if (grid[r][c] < availableValue) {
        ans += (availableValue-grid[r][c])
        grid[r][c] = availableValue
      }
    }
  }
  return ans
};

var getRowMaxVal = function(grid, curR, curC) {
  let val = grid[curR][curC]
  for (let c in grid) {
    if (val < grid[curR][c]) {
      val = grid[curR][c]
    }
  }
  return val
}

var getColMaxVal = function(grid, curR, curC) {
  let val = grid[curR][curC]
  for (let r in grid) {
    if (val < grid[r][curC]) {
      val = grid[r][curC]
    }
  }
  return val
}