var findCircleNum = function(isConnected) {
  // sol1 138ms 21%
  let ans = 0; let visited = []
  var solve = function(idx) {
    for (let i in isConnected[idx]) {
      if (isConnected[idx][i] == 1 && visited.indexOf(i) < 0) {
        visited.push(i)
        solve(i)
      }
    }
  }
  for (let i in isConnected) {
    if (visited.indexOf(i) < 0) {
      visited.push(i)
      solve(i)
      ans += 1
    }
  }
  return ans
};

console.log(findCircleNum([[1,1,0],[1,1,0],[0,0,1]]))