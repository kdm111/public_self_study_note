var grayCode = function(n) {
  // sol2 129ms 45% 51.9MB 86%
  let ans = []
  for (let i=0; i < 2**n; i++) {
    ans.push(i ^ i >> 1)
  }  
  return ans
};

console.log(grayCode(2))