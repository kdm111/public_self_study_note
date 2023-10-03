var rob = function(nums) {
  // sol1
  // const dp = new Array(nums.length+1).fill(-1)  
  // dp[0] = 0; dp[1] = nums[0]
  // for (let i = 1; i < nums.length; i++) {
  //   dp[i+1] = Math.max(dp[i-1] + nums[i], dp[i])
  // }
  // return dp[dp.length-1]

  // sol2 55ms 58% 41.8MB 51%
  // if (nums.length === 1) {
  //   return nums[0]
  // }
  // const dp = new Array(nums.length).fill(-1)
  // dp[0] = nums[0]; dp[1] = Math.max(dp[0], nums[1])
  // for (let i = 2; i < nums.length; i++) {
  //   dp[i] = Math.max(dp[i-2]+nums[i], dp[i-1])
  // }
  // return dp[dp.length-1]
};
// console.log(rob([1,2,3,1]))
console.log(rob([2,1,1,2]))
console.log(rob([2,1]))

// console.log(rob([0]))
