var findLength = function(nums1, nums2) {
  // sol1 246ms 91% 70.9MB 76%
  let dp = Array(nums1.length + 1).fill(0)
  for (let i=0; i < nums1.length+1;i++) {
    dp[i] = Array(nums2.length+1).fill(0)
  }
  let ans = 0
  for (let idx1=nums1.length-1; idx1 >= 0; idx1--) {
    for (let idx2=nums2.length-1; idx2 >= 0; idx2--) {
      if (nums1[idx1] == nums2[idx2]) {
        dp[idx1][idx2] = dp[idx1+1][idx2+1]+1
        ans= Math.max(dp[idx1][idx2], ans)
      }
    }
  }
  return ans
};

console.log(findLength([5, 1, 2, 3, 4], [1, 2, 3, 4, 5]))