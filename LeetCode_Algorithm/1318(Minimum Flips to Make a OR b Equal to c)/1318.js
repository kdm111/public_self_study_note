var minFlips = function(a, b, c) {
  // sol1 43ms 94% 41.3MB 90%
  let ans = 0
  while (a > 0 || b > 0 || c > 0) {
    let x = (a & 1)
    let y = (b & 1)
    let z = (c & 1)
    if ((x | y) != z) {
      if (z == 1) {
        ans += 1
      } else {
        if (x != z) {
          ans += 1
        }
        if (y != z) {
          ans += 1
        }
      }
    } 
    a >>= 1; b >>= 1; c >>= 1
  }
  return ans
};

console.log(minFlips(1,2,3))