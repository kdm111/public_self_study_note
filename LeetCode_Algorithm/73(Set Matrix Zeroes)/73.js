var setZero = (r,c,matrix) => {
  dr = [0,1,0,-1]
  dc = [1,0,-1,0]
  for (let i=0; i < 4; i++){
    newR = r+dr[i]; newC = c+dc[i]
    while ( 0 <=newR && newR < matrix.length && 0 <= newC && newC < matrix[0].length) {
      matrix[newR][newC] = 0
      newR += dr[i]; newC += dc[i]
    }
  }
}
var setZeroes = function(matrix) {
  // sol1 90ms 74% 45MB 57%
  zero = []
  for (let r =0; r < matrix.length; r++) {
    for (let c=0; c <matrix[0].length; c++) {
      if(matrix[r][c] == 0)
        zero.push([r,c]) 
    }
  }
  for (let [r,c] of zero) {
    setZero(r,c,matrix)
  }
};