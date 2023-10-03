var transpose = function(i, matrix) {
  for (let j=0; j < i; j++) {
    let temp = matrix[i][j]
    matrix[i][j] = matrix[j][i]
    matrix[j][i] = temp
  }
}
var rotate = function(matrix) {
  // 78ms 70%
  // transpose
  for (let i=0; i < matrix.length;i++) {
    transpose(i, matrix)
  }

  // reverse
  let l = matrix.length-1
  for (let i=0; i < matrix.length; i++) {
    for (let j=0; j < matrix.length/2;j++) {
      let temp = matrix[i][l-j]
      matrix[i][l-j] = matrix[i][j]
      matrix[i][j] = temp
    }
  }
  return matrix
};

console.log(rotate([[1,2,3],[4,5,6],[7,8,9]]))