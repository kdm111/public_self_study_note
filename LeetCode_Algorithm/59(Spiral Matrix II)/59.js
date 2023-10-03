var solve = (i, k) => {
  for (let c = i; c < k+1; c++) {
    ans[i][c] = val
    val += 1
  }
  for (let r = i+1; r < k+1; r++) {
    ans[r][k] = val
    val += 1
  }
  for (let c=k-1; c >= i; c--) {
    ans[k][c] = val
    val += 1
  }
  for (let r=k-1; r > i; r--) {
    ans[r][i] = val
    val += 1
  }
}
var generateMatrix = function(n) {
  // sol1 59ms 89% 42.8MB 13%
  ans = Array(n).fill(0).map(()=>Array(n).fill(0))
  val = 1; let i = 0
  while (i < n - i) {
    solve(i, n-i-1)
    i += 1
  }
  return ans
};

console.log(generateMatrix(3))