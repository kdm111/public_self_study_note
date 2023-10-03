var numSubarrayProductLessThanK = function(nums, k) {
  // sol2 107ms 46% 47.8MB 51%
  if (k <= 1)
    return 0
  let ans = 0
  let left = 0
  let temp = 1;
  for (let right=0; right < nums.length; right++) {
    temp *= nums[right]
    while (temp >= k) {
      temp /= nums[left]
      left += 1
    }
    ans += (right - left + 1)
  }  
  return ans
};