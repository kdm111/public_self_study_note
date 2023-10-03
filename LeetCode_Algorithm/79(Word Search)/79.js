/**
 * @param {character[][]} board
 * @param {string} word
 * @return {boolean}
 */
 var exist = function(board, word) {
  // sol4 267ms 99% 48.6MB 36%
  const m = board.length; const n = board[0].length
  if (m * n < word.length) { return false }
  let counter = new Map()
  for (let w of word) {
    if (counter[w]) {
      counter[w] += 1
    } else{
      counter[w] = 1
    }
  }
  if (counter[word[0]] > counter[word[word.length-1]]) {
    word = word.split('').reverse().join('')
  }
  var dfs = function(r, c, i) {
    if (i == word.length) {
      return true
    }
    if (r < 0 || r >= m || c < 0 || c >= n || board[r][c] != word[i]) {
      return false
    }
    let dir = [[0,1],[1,0],[0,-1],[-1,0]]
    ret = false
    let temp = board[r][c]
    board[r][c] = '.'
    for (let d=0; d < dir.length; d++) {
      ret = ret || dfs(r+dir[d][0], c+dir[d][1], i + 1)
    }
    board[r][c] = temp
    return ret
  }
  for (let r = 0; r < m; r++) {
    for (let c = 0; c < n; c++) {
      if (dfs(r, c, 0)) {
        return true
      }
    }
  }
  return false
  
};