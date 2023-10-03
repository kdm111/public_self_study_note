var combinationSum3 = function(k, n) {
  // sol1 47ms 98% 42.1MB 62%
  let ans = []
  let solve = (temp, start, totalSum) => {
    if (temp.length == k && totalSum == n) {
      ans.push(temp.slice(0, )); return ;
    }
    for (let num=start; num < 10; num++) {
      if (totalSum + num <= n) {
        temp.push(num)
        solve(temp, num+1, totalSum+num)
        temp.pop()
      } else {
        break
      }
    }
  }
  solve([], 1, 0)
  return ans
};