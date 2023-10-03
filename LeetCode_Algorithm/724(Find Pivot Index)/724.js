
var pivotIndex = function(nums) {
  // sol1 O(n^2), O(1) 964~1191ms 5%
  // for (let i=0; i<nums.length; i++){
  //   let leftIdx = 0
  //   let rightIdx = i+1;
  //   let leftSum = rightSum = 0

  //   while (leftIdx < i){
  //     leftSum += nums[leftIdx]
  //     leftIdx += 1
  //   }
  //   while (rightIdx < nums.length){
  //     rightSum += nums[rightIdx]
  //     rightIdx += 1
  //   }
  //   if (leftSum == rightSum){
  //     return i
  //   }
  // }
  // return -1

  // sol2 O(n), O(1) 76~108ms 90~53%
  let totalSum = nums.reduce((acc, initVal) => {return acc + initVal}, 0)
  let temp = 0
  for (let i = 0; i < nums.length; i++) {
      totalSum -= nums[i]
      if (totalSum == temp) {
          return i
      }
      temp += nums[i]
  }
  return -1
};

console.log(pivotIndex([1,2,3]))