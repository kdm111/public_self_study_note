var isPowerOfFour = function(n) {
  // 112ms 42%
  if (n == 0) {
    return false
  }
  while (n % 4 == 0) {
    n /= 4
  }  
  return n ==1 ? true : false
};