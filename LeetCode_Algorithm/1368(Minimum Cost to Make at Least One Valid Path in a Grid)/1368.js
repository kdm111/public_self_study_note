var minCost = function(grid) {
  // sol3 167ms 82%
  // dp dfs bfs
  m = grid.length; n = grid[0].length
  dp = Array.from(new Array(m), () => new Array(n).fill(10*1000))
  dir = [[0,1],[0,-1],[1,0],[-1,0]]
  queue = []
  dfs(0,0,0, grid)
  while (queue.length) {
    [r,c]= queue.shift()
    if (r == m-1 && c == n-1) {
      return dp[r][c]
    }
    for (let [i,j] of dir) {
      if (0 <= r+i && r+i < m && 0<= c+j && c+j < n) {
        dfs(r+i, c+j, dp[r][c]+1, grid)
      }
    }
  }
};
var dfs = function(r,c,k, grid) {
  if (0 <= r && r < m && 0 <= c && c < n && dp[r][c] > k) {
    dp[r][c] = k
    queue.push([r,c])
    dfs(r+dir[grid[r][c]-1][0], c+dir[grid[r][c]-1][1], k, grid)
  }
}
console.log(minCost([[1,1,1],[2,2,2],[1,1,1],[2,2,2]]))
