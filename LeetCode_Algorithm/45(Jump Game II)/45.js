var jump = function(nums) {
  // sol1 66ms 93% 43.6MB 90%
  if (nums.length == 1)
    return 0;
  let canJump = 0; let ans = 0; let far = 0
  for (let i=0; i < nums.length; i++) {
    if (i > canJump) {
      ans += 1
      canJump = far
    }
    far = Math.max(far, nums[i]+i)
  }  
  return ans
};