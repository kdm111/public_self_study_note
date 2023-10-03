var searchInsert = function(nums, target) {
  // sol1 118ms 7%
  // let left = 0; let right = nums.length-1
  // while (left <= right) {
  //   let mid = left + parseInt((right-left)/2)
  //   if (nums[mid] == target) {
  //     return mid
  //   } else if (nums[mid] < target) {
  //     left = mid+1
  //   } else {
  //     right = mid-1
  //   }
  // }
  // return left

  // sol2 94ms 44%
  nums.push(target)
  nums.sort((a,b) => {return a-b})
  return nums.indexOf(target)
};