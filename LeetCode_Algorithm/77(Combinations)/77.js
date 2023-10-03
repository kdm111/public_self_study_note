var solve = (n, k, temp, idx) => {
  if (temp.length == k) {
    ans.push(temp.slice(0, ))
    return ;
  }
  for (let i=idx; i <= n; i++) {
    temp.push(i)
    solve(n, k, temp, i+1)
    temp.pop()
  }
}
var combine = function(n, k) {
  // sol1 93ms 99% 46.7MB 88%
  ans = []
  solve(n, k, [], 1)
  return ans
};