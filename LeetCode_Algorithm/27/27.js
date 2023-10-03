var removeElement = function(nums, val) {
  // sol1 51ms 92% 41.4MB 97%
  let i = 0; let ans = 0
  while (i < nums.length) {
    if (nums[i] == val) {
      nums.splice(i, 1)
      nums.push(-1)
      ans += 1;
      continue
    }
    i += 1
  }  
  return nums.length-ans
};