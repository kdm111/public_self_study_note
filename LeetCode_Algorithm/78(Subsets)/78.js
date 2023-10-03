var solve = (nums, idx, temp) => {
  ans.push(temp.slice(0, ))
  for (let i=idx; i < nums.length; i++) {
    temp.push(nums[i])
    solve(nums, i+1, temp)
    temp.pop()
  }
}
var subsets = function(nums) {
  // sol1 74ms 69% 42.6MB 95%
  ans = []
  solve(nums, 0, [])
  return ans 
};

console.log(subsets([1,2,3]))