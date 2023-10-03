var canJump = function(nums) {
  // sol4 75ms 94% 46.3MB 60%
  let goal = nums.length-1
  for (let i = nums.length-1; i >= 0; i--) {
    if (i + nums[i] >= goal) {
      goal = i
    }
  }  
  return goal == 0
};