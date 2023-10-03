var hammingDistance = function(x, y) {
  // sol3 67ms 90% 41.8MB 81%
  let xor = x ^ y
  let ans = 0
  while (xor) {
    if (xor & 1) {
      ans += 1
    }
    xor >>= 1
  }  
  return ans
};