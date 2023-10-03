var shortestPathBinaryMatrix = function(grid) {
  // sol1 776ms 5% 59.7MB 6%
  if (grid[0][0] == 1)
    return -1
  let directions = [[0,1], [1,1], [1,0], [1,-1], [0,-1], [-1,-1], [-1,0], [-1,1]]
  let queue = [[0, 0, 1]]; let seen = new Set(["0,0"])
  while (queue.length) {
    [r, c, cnt]= queue.shift()
    if (r == grid.length-1 && c == grid[0].length-1)
      return cnt
    for (let [dr, dc] of directions) {
      let newR = r + dr; let newC = c + dc
      if (0 <= newR && newR < grid.length && 0 <= newC && newC < grid[0].length) {
        // console.log(newR, newC, !seen.has(String(newR) + ',' + String(newC) && grid[newR][newC] == 0))
        if (grid[newR][newC] == 0 && !seen.has(String(newR) + ',' + String(newC))) {
          console.log(newR, newC)
          seen.add(String(newR) + ',' + String(newC))
          queue.push([newR, newC, cnt+1])
        }
      }
    }
  }
  return -1
};
console.log(shortestPathBinaryMatrix([[0,0,0],[1,1,0],[1,1,0]]))
// [0,0,0],
// [1,1,0],
// [1,1,0]