var findMaxConsecutiveOnes = function(nums) {
  // sol1 78ms 46% 45MB 18%
  let ans = 0; let temp = 0
  for (let num of nums) {
    if (num == 1)
      temp += 1
    else {
      ans = Math.max(ans, temp)
      temp = 0
    }
  }
  ans = Math.max(ans, temp)
  return ans
};