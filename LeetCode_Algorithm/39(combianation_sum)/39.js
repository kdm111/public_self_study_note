var solve = function(candidates_sliced, path, target, ans) {
  if (target < 0) {
    return ;
  }
  if (target == 0) {
    ans.push(path); return ;
  }

  for (let i in candidates_sliced) {
    let path_temp = path.slice(); path_temp.push(candidates_sliced[i])
    solve(candidates_sliced.slice(i, ),path_temp, target-candidates_sliced[i], ans)
  }
}

var combinationSum = function(candidates, target) {
  // sol1 204ms 7%
  candidates.sort((a,b) => {
    return a-b
  })
  let ans = []
  for (let i in candidates) {
    let temp = candidates.slice(i, )
    solve(temp, [candidates[i]], target-candidates[i], ans)
  }
  return ans
};

console.log(combinationSum([2,3,5], 8))