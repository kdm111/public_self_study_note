var buildArray = function(nums) {
  // sol1 88ms 61% 46.1MB 43%
  // let ans = []
  // for (let i=0; i < nums.length; i++) {
  //   ans.push(nums[nums[i]])
  // }
  // return ans

  // sol2 89ms 59% 45.7MB 69%
  for (let i=0; i < nums.length; i++) {
    if (nums[i] < nums.length) {
      nums[i] = nums[i] + nums.length * (nums[nums[i]] % nums.length)
    }
  }
  for (let i = 0; i < nums.length; i++) {
    nums[i] = parseInt(nums[i] / nums.length)
  }
  return nums
};