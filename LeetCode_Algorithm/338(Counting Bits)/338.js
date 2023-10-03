var countBits = function(n) {
  // sol4 T : 133ms 75% S : 48M 84%
  let ans = new Array(n+1).fill(0)
  let b = 1
  let num = 0
  while (b <= n)  {
    while (num + b <= n) {
      ans[num + b] = ans[num] + 1
      num += 1
    }
    num = 0
    b <<= 1
  } 
  return ans
};
console.log(countBits(5))