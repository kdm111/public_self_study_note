var minSubArrayLen = function(target, nums) {
  // sol1 63ms 77% 45.9MB 75%
  let total = 0; let i = 0
  let ans = Infinity
  for (let j = 0; j < nums.length; j++) {
    total += nums[j]
    while (total >= target) {
      ans = Math.min(ans, j-i+1)
      total -= nums[i]
      i += 1
    }
  }
  return ans == Infinity ? 0 : ans
};