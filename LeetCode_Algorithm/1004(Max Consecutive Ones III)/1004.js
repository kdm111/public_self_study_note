var longestOnes = function(nums, k) {
  // sol2 77ms 47% 47.1MB 55%
  let left = right = ans = 0
  while (right < nums.length) {
    if (nums[right] == 0) {
      k -= 1
    }
    while (k < 0 && left < nums.length) {
      if (nums[left] ==0) {
        k += 1
      }
      left += 1
    }
    ans = Math.max(ans, right-left+1)
    right += 1
  }
  return ans
};