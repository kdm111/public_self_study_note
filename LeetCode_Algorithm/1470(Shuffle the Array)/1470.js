var shuffle = function(nums, n) {
  // sol1 61ms 97% 44.6MB 34%
  for (let i = n; i < nums.length; i++) {
    nums[i] = nums[i] << 10 | nums[i-n]
  }  
  let i = 0
  for (let j = n; j < nums.length; j++) {
    nums[i] = nums[j] & 1023
    nums[i+1] = nums[j] >> 10
    i += 1
  }
  return nums
};