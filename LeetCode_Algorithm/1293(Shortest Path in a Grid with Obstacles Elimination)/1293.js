var toRCDSeen = (r, c, d) => {
  return String(r) + ',' + String(c) + ',' + String(d)
}
var shortestPath = function(grid, k) {
  // sol1 119ms 81% 50MB 68%1
  let seen = new Set(); let ans = Infinity
  let directions = [[0,1], [1,0], [0,-1], [-1, 0]]
  let queue = [[0, 0, 0, k]]; let m = grid.length; let n = grid[0].length
  if (k > m + n - 2) {
    return m +n - 2
  }
  while (queue.length) {
    [r, c, cnt, d] = queue.shift()
    if (cnt >= ans)
      continue
    if (r == m - 1 && c == n - 1) {
      ans = Math.min(ans, cnt)
      continue
    }
    for (let [dr, dc] of directions) {
      let mvR = r + dr; let mvC = c + dc
      if (mvR >= 0 && mvR < m && mvC >= 0 && mvC < n && !seen.has(toRCDSeen(mvR,mvC,d))) {
        seen.add(toRCDSeen(mvR, mvC, d))
        if (grid[mvR][mvC] == 0)
          queue.push([mvR, mvC, cnt+1, d])
        if (grid[mvR][mvC] == 1 && d > 0)
          queue.push([mvR, mvC, cnt+1, d-1])
      }
    }
  }
  return ans != Infinity ? ans : -1
};