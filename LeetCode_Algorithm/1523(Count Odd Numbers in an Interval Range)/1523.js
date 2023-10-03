var countOdds = function(low, high) {
  // sol1 4741ms 33%
  // let ans = 0
  // while (low != high+1) {
  //   if (low %2 == 1){
  //     ans += 1
  //   }
  //   low+=1
  // }
  // return ans
  // sol2 75ms 86%
  if (low % 2 == 1) {
    low -=1 
  }  
  if (high % 2 == 1){
    high += 1
  }
  return parseInt((high-low) / 2)
};