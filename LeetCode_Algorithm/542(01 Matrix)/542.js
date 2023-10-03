var updateMatrix = function(mat) {
  // sol 322ms 45%
  // bfs 
  let queue = []
  for (let r=0; r < mat.length; r++) {
    for (let c=0; c < mat[0].length; c++) {
      if (mat[r][c] == 0) {
        queue.push([r,c])
      } else{
        mat[r][c] = -1
      }
    }
  }
  const dr =[0,1,0,-1]
  const dc = [1,0,-1,0]
  while (queue.length) {
    [r,c] = queue.shift()
    for (let i=0; i < 5; i++) {
      let newR = r+dr[i]
      let newC = c+dc[i]
      if (newR < 0 || newR > mat.length || newC< 0 || newC > mat[0].length || mat[newR][newC] != -1) {
        continue
      }
      mat[newR][newC] = mat[r][c]+1
      queue.push([newR, newC])
    }
  }
  return mat
};