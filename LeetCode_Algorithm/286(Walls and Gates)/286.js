
var wallsAndGates = function(rooms) {
  // sol1 1114ms 15%
  // 
  if (rooms.length == 0) {
    return []
  }
  const m = rooms.length; const n = rooms[0].length
  let q = []
  for (let r=0; r < m; r++) {
    for (let c=0; c < n; c++) {
      if (rooms[r][c] == 0) {
        q.push([r,c])
      }
    }
  }
  while (q.length) {
    [r,c] = q.shift()
    for (let [dr,dc] of [[0,1], [1,0], [0,-1],[-1,0]]) {
      const newR = r+dr; const newC = c+dc
      // newR
      if (newR < 0 || newR >= m || newC < 0 || newC >= n || rooms[newR][newC] != 2147483647) {
        continue
      }
      rooms[newR][newC] = rooms[r][c] + 1
      q.push([newR, newC])
    }
  }
  return rooms
};

console.log(wallsAndGates([[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]))