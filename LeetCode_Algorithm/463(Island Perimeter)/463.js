var islandPerimeter = function(grid) {
  // sol1 281ms 46% 51.5MB 28%
  let ans = 0
  for (let r = 0; r < grid.length; r++) {
    for (let c = 0; c < grid[0].length; c++) {
      if (grid[r][c] == 1) {
        cnt = 4
        for (let [i,j] of [[0,1],[1,0],[0,-1], [-1,0]]) {
          if (0 <= r+i && r+i < grid.length && 0 <= c+j && c+j < grid[0].length) {
            if (grid[r+i][c+j] == 1) {
              cnt -= 1
            } 
          }
        }
        ans += cnt
      }
    }
  }  
  return ans
};