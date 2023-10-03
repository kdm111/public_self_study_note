var threeConsecutiveOdds = function(arr) {
  // sol1 70ms 80% 41.3MB 99%  
  let cnt = 0
  for (let num of arr) {
    if (num % 2 == 1) {
      cnt += 1
    } else {
      cnt = 0
    }
    if (cnt == 3) {
      return true
    }
  }  
  return false
};