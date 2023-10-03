var getConcatenation = function(nums) {
  // sol1 71ms 98% 45.1MB 74%
  // return nums.concat(nums)
  // sol2 83% 88% 44.8MB 89%
  let ans = new Array(2 * nums.length)
  for (let i=0; i < nums.length; i++) {
    ans[i] = nums[i]
    ans[i+nums.length] = nums[i]
  }
  return ans
};