var firstMissingPositive = function(nums) {
  // sol1 92ms 63% 51.6MB 35%
  for (let i=0; i < nums.length; i++ ){
    if (nums[i] <= 0 || nums[i] > nums.length)
      nums[i] = 0
  }
  let arr = new Array(Math.max(...nums)).fill(0)
  arr[0] = 1
  for (let i=0; i <nums.length; i++) {
    arr[nums[i]] = 1
  }
  for (let i=0; i < nums.length; i++) {
    if (arr[i] == 0)
      return i
  }
  return arr.length
};