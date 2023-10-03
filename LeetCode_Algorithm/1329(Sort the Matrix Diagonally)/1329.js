var solve = function(mat, r, c) {
  
  let i = r; let j = c
  let temp = []
  while (i < mat.length && j < mat[0].length) {
    temp.push(mat[i][j]); i++; j++
  } 
  temp.sort((a,b)=>{return a-b}); i = 0
  while (r < mat.length && c < mat[0].length) {
    mat[r][c] = temp[i];
    r++;c++;i++
  }
}

var diagonalSort = function(mat) {
  // 84ms 97%
  let m = mat.length; let n = mat[0].length
  for (let r=0; r < m; r++) {
    solve(mat,r, 0)
  }
  for (let c=1; c<n; c++) {
    solve(mat,0,c)
  }
  return mat
};

console.log(diagonalSort([[11,25,66,1,69,7],[23,55,17,45,15,52],[75,31,36,44,58,8],[22,27,33,25,68,4],[84,28,14,11,5,50]]))