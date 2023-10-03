var gameOfLife = function(board) {
  // sol1 46ms 90% 41.5MB 91%
  const d = [[-1, 0], [-1, 1], [0,1], [1,1], [1,0], [1,-1], [0,-1], [-1,-1]]
  const setZero = new Set()
  const setOne = new Set()
  for (let r = 0; r < board.length; r++) {
    for (let c = 0; c < board[0].length; c++) {
      let cntOne = 0
      for (let k = 0; k < 8; k++) {
        let newR = r + d[k][0]
        let newC = c + d[k][1]
        if (0 <= newR && newR < board.length && 0 <= newC && newC < board[0].length) {
          if (board[newR][newC] == 1)
            cntOne += 1
        }
      }
      if (cntOne == 3 && board[r][c] == 0) {
        setOne.add([r,c])
      }
      if ((cntOne > 3 || cntOne < 2) && board[r][c] == 1) {
        setZero.add([r,c])
      }
    }
  }
  for (let [r,c] of setOne) {
    board[r][c] = 1
  }
  for (let [r,c] of setZero) {
    board[r][c] = 0
  }
};