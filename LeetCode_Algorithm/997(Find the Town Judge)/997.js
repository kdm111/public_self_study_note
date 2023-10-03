var findJudge = function(n, trust) {
  // sol1 101ms 84% 50.6MB 67%
  let arr = new Array(n+1).fill(0)
  for (let [i,j] of trust) {
      arr[i] -= 1
      arr[j] += 1
  }
  for (let i=1; i <= n; i++) {
      if (arr[i] == n-1)
          return i
  }
  return -1
};