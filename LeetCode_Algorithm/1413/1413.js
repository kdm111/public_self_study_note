var minStartValue = function(nums) {
  // sol1 O(n), O(1) 88~97ms 45~28%
  var ans = 0
  var minValue = 0
  for (let num of nums) {
    minValue += num
    ans > minValue ? ans = minValue : ans = ans
  }
  return Math.abs(ans)+1
};

console.log(minStartValue([1,-2,-3]))