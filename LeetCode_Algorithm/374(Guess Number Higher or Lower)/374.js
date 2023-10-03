var guessNumber = function(n) {
  // 87ms 65% 42.3MB 10.6%
  let left = 1; let right = n
  while (true) {
    let mid = left + parseInt((right-left) / 2)
    let res = guess(mid)
    if (res == -1) {
      right = mid-1 
    } else if (res == 1) {
      left = mid+1
    } else {
      return mid
    }
  }  
};