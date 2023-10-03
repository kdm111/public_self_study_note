var arraySign = function(nums) {
  // sol1 49ms 96% 44.2MB 30%
  let ans = 1
  for (let num of nums) {
      if (num == 0) {
          return 0
      } else if (num < 0) {
          ans *= -1
      }
  }
  return ans
};