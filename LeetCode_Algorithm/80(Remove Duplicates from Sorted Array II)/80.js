var removeDuplicates = function(nums) {
  // sol1 72ms 45% 44.7MB 17%
  let ret = nums.length
  let cur = nums[ret-1]; let cnt = 0
  for (let i = nums.length; i >= 0; i--) {
    if (nums[i] == cur) {
      cnt += 1 } else{
      cnt = 1
    }
    if (cnt > 2) {
      ret -= 1
      nums.splice(i, 1)
      nums.push(-1)
    }
    cur = nums[i]
  }
  return ret
};
console.log(removeDuplicates([1,1,1,2,2,3]))