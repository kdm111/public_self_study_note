var longestSubarray = function(nums) {
  // sol1 73ms 40% 46.3MB 47%
  if (new Set(nums).length == 1) {
    if (nums[0] == 1)
      return nums.length - 1
    else
      return 0
  }
  let cnt0 = 0; let l = 0; let r = 0
  let ans = 0
  while (r < nums.length) {
    if (nums[r] == 0) {
      cnt0 += 1
    }
    while (cnt0 == 2) {
      if (nums[l] == 0)
        cnt0 -= 1
      l += 1
    }
    ans = Math.max(ans, r-l)
    r += 1
  }  
  return ans
};