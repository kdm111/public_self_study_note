/**
 * @param {character[][]} board
 * @return {boolean}
 */
 var rowValid = function(row, col) {
  for (let c = 0; c < board[0].length; c++) {
    if (c != col) {
      if (board[row][col] == board[row][c]) {
        return false
      }
    }
  }
  return true
}
var colValid = function(row, col) {
  for (let r = 0; r < board.length; r++) {
    if (r != row) {
      if (board[row][col] == board[r][col]) {
        return false
      }
    }
  }
  return true  
}
var cubeValid = function(row, col) {
  const cubeR = parseInt(row / 3) * 3
  const cubeC = parseInt(col / 3) * 3

  for (let r = cubeR; r < cubeR + 3; r++) {
    for (let c = cubeC; c < cubeC + 3; c++) {
      if (row != r && col != c) {
        if (board[row][col] == board[r][c]) {
          return false
        }
      }
    }
  }
  return true
}
var valid = function(row, col) {
  if (board[row][col] == '.') {
    return true
  }
  if (rowValid(row, col) && colValid(row, col) && cubeValid(row, col)) {
    return true
  }
  return false
}

var isValidSudoku = function(board) {
  // sol1 145ms 31% 45.7MB 48%
  globalThis.board = board
  let row = 0;
  let col = 0
  while (valid(row, col)) {
    col += 1
    if (col == board[0].length) {
      row += 1; col = 0
    }
    if (row == board.length) {
      return true
    }
  }
  return false
};