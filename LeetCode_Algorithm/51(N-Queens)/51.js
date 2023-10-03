var solveNQueens = function(n) {
  // sol1 126ms 50%
  ans = []
  board = Array.from(new Array(n), () =>new Array(n).fill('.'))
  dfs(0)
  return ans
};
var dfs = function(r) {
  if (r == board.length) {
    let temp = []
    for (let i=0; i < board.length; i++) {
      temp.push(board[i].join(''))
    }
    ans.push(temp)
    return ;
  }
  for (let c=0; c < board.length; c++) {
    if (board[r][c] != 'Q') {
      board[r][c] = 'Q'
      if (check(r-1, c)) {
        dfs(r+1)
      }
      board[r][c] = '.'
    }
  }
}
var check = function(r,c) {
  let slash = c+1; let backSlash = c-1

  while (-1 < r) {
    if (board[r][c] == 'Q') {
      return false
    } else if (slash < board.length && board[r][slash] == 'Q') {
      return false
    } else if (-1 < backSlash && board[r][backSlash] == 'Q'){
      return false
    }
    r -= 1; slash += 1; backSlash -= 1
  }
  return true
}

console.log(solveNQueens(5))