var missingNumber = function(nums) {
  
  // sol1 O(n), O(1) 65~98ms 92~54%
  // gauss summation
  // var length = nums.length
  // sumNums = parseInt(length*(length+1) / 2)
  // var currSum = nums.reduceRight(function(sum,currVal){
  //   return (sum+currVal)}, 0)
  // return sumNums-currSum

  // sol2 O(n), O(n) 80~138ms 77~21%
  // set과 hashmap
  // hashMap = new Set(nums)
  // for (let idx=0; idx<=nums.length; idx++){
  //   if (!hashMap.has(idx)){return idx}
  // }

  // sol3 O(n), O(1) 72~132ms 86~24%
  // 비트 조작
  var missing = nums.length
  // ES6
  // for (const [idx, num] of nums.entries()) {
  //   missing ^= idx ^ num
  // }
  // return missing
  
  // ES5 76~123ms 81~29%
  const arr = nums.map(function(num, idx){
    return [idx, num]
  })
  for (const [idx, num] of arr){
    missing ^= idx ^ num
  }
  return missing


  
};
console.log(missingNumber([2,0,1]))