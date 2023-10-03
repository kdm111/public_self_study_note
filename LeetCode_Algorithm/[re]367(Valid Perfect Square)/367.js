
var isPerfectSquare = function(num) {
  // sol1 115ms 21%
  if (num == 1) {
    return true
  }
  let left = 2; let right = parseInt(num / 2);
  while (left <= right) {
    let mid = left + parseInt((right-left)/2)
    if (mid * mid == num) {
      return true
    } else if (mid * mid < num) {
      left = mid + 1
    } else {
      right = mid - 1
    }
  }
  return false
};