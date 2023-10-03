binary_search = function(nums, left, right, target) {
  while (left < right || left == right) {
    let mid = left + parseInt((right-left)/2)
    if (nums[mid] == target) {
      return mid
    } else {
      if (nums[mid] < target) {
        left = mid+1
      } else {
        right = mid-1
      }
    }
  }
  return -1
}
var search = function(nums, target) {
  // sol1 O(logn) O(1) 71ms 80%
  let pivotIdx = 0;
  if (nums.length == 1) {
    let ret = nums[0] == target ? 0 : -1; return ret
  }
  let left = 0; let right = nums.length-1
  while (left < right || left == right) {
    let mid = left + parseInt((right-left) /2)
    // js에서 숫자 크기를 비교하기 위해 parseInt 사용
    if ((mid == left || parseInt(nums[mid-1]) > parseInt(nums[mid])) && (mid == right || parseInt(nums[mid]) < parseInt(nums[mid+1]))) {
      pivotIdx = mid; break
    } else {
      if (nums[mid] > nums[right]) {
        left = mid+1
      } else {
        right = mid-1
      }
    }
  }
  let ans = binary_search(nums, 0, pivotIdx-1, target)
  if (ans != -1) {return ans} 
  return binary_search(nums, pivotIdx, nums.length-1, target)
};

console.log(search([3,4,5,6,1,2], 2))
// console.log(search([1,2,3,5,6], 5))
// console.log(search([6,5,4,3,2,1], 4))

// console.log(search([0], 0))