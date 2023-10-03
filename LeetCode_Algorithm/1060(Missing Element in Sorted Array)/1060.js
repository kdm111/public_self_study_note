var missing = function(nums, idx) {
  return nums[idx] - (nums[0]+idx)
}
var missingElement = function(nums, k) {
  // 110ms 50%
  let idx = 1
  while (idx < nums.length && missing(nums,idx) < k) {
    idx += 1
  }
  return nums[idx-1] + k - missing(nums, idx-1)
 };