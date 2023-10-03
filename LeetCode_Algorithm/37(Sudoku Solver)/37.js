var availableNum = function(board, row, col) {
  seen = new Set()
  for (let c=0; c < 9; c++) {
    seen.add(board[row][c])
  }
  for (let r=0; r < 9; r++) {
    seen.add(board[r][col])
  }
  let tempR  = parseInt(row / 3) * 3
  let tempC = parseInt(col / 3) * 3
  for (let r= tempR; r < tempR+3; r++) {
    for (let c=tempC; c<tempC+3; c++) {
      seen.add(board[r][c])
    }
  }
  // length 9인 배열 생성 뒤 idx를 뽑아 +1에서 리턴
  nums = [...Array(9).keys()].map(i => i+1)
  nums = Array.from({length : 9}, (_, i) => i+1)
  
  let ret = []
  for (let num of nums) {
    if (!seen.has(String(num))) {
      ret.push(String(num))
    }
  }
  return ret
}
var backtracking = function(board, row, col) {
  while (board[row][col] != '.') {
    col += 1
    if (col == 9) {
      row += 1; col = 0
    }
    if (row == 9) {
      return true
    }
  }
  let stack = availableNum(board, row, col)
  for (let num of stack) {
    board[row][col] = num
    if (backtracking(board, row, col)) {
      return true
    }
  }
  board[row][col] = '.'
  return false
}
var solveSudoku = function(board) {
    // sol1 327ms 14%
    // 9! 9!
    backtracking(board, 0, 0)
};
