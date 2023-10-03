var runningSum = function(nums) {
  // sol1 O(n)
  // 68ms 86%
  // let ans = []
  // let temp = 0
  // for (let num of nums) {
  //   temp += num
  //   ans.push(temp)
  // }
  // return ans

  // sol2 O(n)
  // 123ms 6%
  for (let idx=1; idx < nums.length; idx++) {
    nums[idx] = nums[idx-1]+nums[idx]
  }
  return nums
};

console.log(runningSum([1,2,3,4]))