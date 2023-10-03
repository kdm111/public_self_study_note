var trailingZeroes = function(n) {
  // sol2 66ms 52% 42.2MB 64%
  let ans = 0
  while (parseInt(n / 5) != 0) {
    ans += parseInt(n / 5)
    n /= 5
  }  
  return ans
};