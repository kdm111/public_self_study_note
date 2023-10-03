var findMin = function(nums) {
  // sol1 75ms 54% 41.8MB 76%
  let left = 0; let right = nums.length-1
  while (left < right) {
    let mid = left + parseInt((right-left)/2)
    if (nums[mid] > nums[right]) {
      left = mid+1
    } else {
      right = mid
    }
  }  
  return nums[left]
};