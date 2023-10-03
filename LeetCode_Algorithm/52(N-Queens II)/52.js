var totalNQueens = function(n) {
  // sol1 T : 115ms 46% S : 42.8MB 63%
  arr = new Array(n).fill(0); ans = 0
  dfs(0)
  return ans
};
var dfs = function(idx) {
  if (idx == arr.length) {
    ans += 1; return ;
  }
  for (let c=1; c < arr.length+1; c++) {
    if (isValid(idx-1, c)) {
      arr[idx] = c
      dfs(idx+1)
    }
  }
}
var isValid = function(row, col) {
  let acc = 1
  while (row >= 0) {
    if (arr[row] == col) {
      return false
    }
    if (arr[row]  == col-acc || arr[row] == col+acc) {
      return false
    }
    row -= 1; acc += 1;
  }
  return true
}
console.log(totalNQueens(10))