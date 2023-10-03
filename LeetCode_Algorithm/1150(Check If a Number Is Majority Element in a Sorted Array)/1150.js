var search = function(nums, target) {
  let left = 0; let right = nums.length
  while (left < right) {
    let mid = left + parseInt((right -left)/2)
    if (nums[mid] < target) {
      left = mid+1
    } else {
      right = mid
    }
  }
  return left
}
var isMajorityElement = function(nums, target) {
  // sol2 64ms 94% 41.8MB 79%
  let low = search(nums, target)
  let high = search(nums, target+1)
  if (nums[parseInt(nums.length / 2)] == target && high - low > parseInt(nums.length / 2)) {
    return true
  }  
  return false
};