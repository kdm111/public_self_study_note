var numIdenticalPairs = function(nums) {
  // sol1 T : 101ms 39% S : 41.8 67%
  let cntArr = new Array(101).fill(0); let ans = 0
  for (let num of nums) {
    ans += cntArr[num]++;
  }  
  return ans
};
console.log(numIdenticalPairs([1,1,1,1]))