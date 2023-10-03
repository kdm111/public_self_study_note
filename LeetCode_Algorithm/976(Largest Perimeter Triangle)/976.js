var largestPerimeter = function(nums) {
  // sol1 170ms 53% 45.8MB 22.3%
  nums.sort((a,b) => {
    return b-a
  })
  for (let i = 0; i < nums.length-2; i++) {
    if (nums[i] < nums[i+1] + nums[i+2]) {
      return nums[i] + nums[i+1] + nums[i+2]
    }
  }
  return 0
};
