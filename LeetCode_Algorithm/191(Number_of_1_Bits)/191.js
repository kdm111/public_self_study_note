var hammingWeight = function(n) {
  // sol2 105ms 40%
  let ans = 0;
  for (let i=0; i < 32; i++) {
    ans += n & 1
    n >>= 1
  } 
  return ans
};

console.log(hammingWeight("00000000000000000000000000001011"))
console.log(hammingWeight("11111111111111111111111111111101"))
