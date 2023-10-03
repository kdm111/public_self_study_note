var partitionArray = function(nums, k) {
  // sol1 219ms 88% 54.4MB 54%
  nums.sort((a,b)=> {return a-b}); let minNum = nums[0]; let ans = 1
  for (let i=1;i < nums.length; i++) {
    if (nums[i] - minNum > k) {
      ans += 1
      minNum = nums[i]
    }
  }
  return ans
};