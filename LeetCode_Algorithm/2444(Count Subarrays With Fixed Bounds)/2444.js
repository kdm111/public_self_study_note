var countSubarrays = function(nums, minK, maxK) {
  // sol1 85ms 73% 49.5MB 40%
  let minIdx = -1; let maxIdx = -1; let ans = 0
  let start = -1
  for (let i = 0; i < nums.length; i++) {
    if (nums[i] < minK || nums[i] > maxK)
      start = i
    if (nums[i] == minK)
      minIdx = i
    if (nums[i] == maxK)
      maxIdx = i
    ans += Math.max(0, Math.min(minIdx, maxIdx) - start)
  }
  return ans
};