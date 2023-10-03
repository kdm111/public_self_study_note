
var maxSubArray = function(nums) {
  // sol1 n^2 시간 초과
  // var ans = -Infinity
  // for(let i=0; i<nums.length; i++){
  //   let currSumArray = 0
  //   for(let j=i;j<nums.length; j++){
  //     currSumArray += nums[j]
  //     if (ans < currSumArray){ans = currSumArray}
  //   }
  // }
  // return ans

  // sol2 n 107ms 64% 보다 빠름 또는 151ms 
  
  var ans = -Infinity
  var currSumArray = 0
  for(let i=0; i < nums.length; i++){
    let temp = currSumArray+nums[i]
    temp < nums[i] ? currSumArray = nums[i] : currSumArray = temp
    ans < currSumArray ? ans = currSumArray : ans = ans 
  }
  return ans

};
console.log(maxSubArray([-2,1,2,3,4,5]))