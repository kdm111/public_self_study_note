var longestConsecutive = function(nums) {
  // sol2 232ms 53% 59.4MB 29%
  if (nums.length == 0)
    return 0
  nums = Array.from(new Set(nums))
  nums.sort((a,b) => {return a-b})
  ans = 1; temp = 1
  for (let i = 1; i < nums.length; i++) {
    if (nums[i-1]+1 == nums[i])
      temp += 1
    else
      temp = 1
    ans = Math.max(ans, temp)
  }
  return ans 
};