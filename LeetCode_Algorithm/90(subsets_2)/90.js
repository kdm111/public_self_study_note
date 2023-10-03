var backtracking = function(nums, path) {
  ans.push(path)
  for (let i=0; i < nums.length; i++) {
    if (i > 0 && nums[i] == nums[i-1]) {
      continue
    }
    let temp = path.slice(0, ); temp.push(nums[i])
    backtracking(nums.slice(i+1, ), temp)
  }
}

var subsetsWithDup = function(nums) {
  // sol1 97ms 62%
  ans = []
  nums.sort((a,b) =>{
    return a-b
  })
  backtracking(nums, [])
  return ans
};

console.log(subsetsWithDup([1,2,2]))