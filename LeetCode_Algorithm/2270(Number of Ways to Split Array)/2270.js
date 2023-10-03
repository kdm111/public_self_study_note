var waysToSplitArray = function(nums) {
  // 103ms 84% 61.9MB 51%
  let prefix = [nums[0]]  
  for (let i = 1; i < nums.length; i++) {
    prefix.push(prefix[prefix.length-1] + nums[i])
  }
  let ans = 0
  for (let i=0 ;i < prefix.length-1; i++) {
    if (prefix[i] >= prefix[prefix.length-1]-prefix[i])
      ans += 1
  }
  return ans
};