var spiralOrder = function(matrix) {
  // sol1 113ms 8%
  const m = matrix.length; const n = matrix[0].length
  let r = 0; let c = 0
  const dr = [0,1,0,-1]; const dc = [1,0,-1,0]
  const ans = [matrix[r][c]]
  const visited = true
  matrix[r][c] = visited
  let currentDir = -1
  while (ans.length < m*n) {
    currentDir = (currentDir+1) % 4 
    while (true) {
      r += dr[currentDir]; c += dc[currentDir]
      if (!(0 <= r && r < m && 0 <= c && c < n)) {
        r -= dr[currentDir]; c -= dc[currentDir]
        break
      }
      if (matrix[r][c] == visited) {
        r -= dr[currentDir]; c -= dc[currentDir]
        break
      }
      ans.push(matrix[r][c])
      matrix[r][c] = visited
    }   
  }
  return ans
};

console.log(spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))