var numPairsDivisibleBy60 = function(time) {
  // sol3 93ms 78% 46.2MB 28%

  let ans = 0; let cntArr = new Array(61).fill(0)
  for (let t of time) {
    if (t % 60 == 0) {
      ans += cntArr[0]
    } else {    
       ans += cntArr[60-(t%60)]
    }
    cntArr[t % 60] += 1
  }
  return ans
  
};