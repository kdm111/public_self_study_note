
var canPartition = function(nums) {
  // sol2 1367ms 18%
  // if (nums.length == 0) {return false}
  // let initialValue= 0
  // let totalSum = nums.reduce(
  //   (prev,curr)=> prev+curr, initialValue // initialValue 가 없으면 빈 배열에서 오류 발생
  // )
  // if (totalSum % 2 == 1){
  //   return false
  // }
  // totalSum = parseInt(totalSum / 2)
  // let lst = new Set()
  // lst.add(nums[0])
  // let temp = new Set()
  // temp.add(nums[0])
  // for (let i=1; i < nums.length; i++) {
  //   lst.forEach((value) => {
  //     temp.add(value+nums[i])
  //   })
  //   lst = new Set(temp)
  // }
  // if (lst.has(totalSum)) {
  //   return true
  // } else {
  //   return false
  // }


  // sol3 351ms 47%
  let totalSum = nums.reduce((prev, curr) => prev+curr, 0)
  if (totalSum % 2 == 1) {return false}
  totalSum = parseInt(totalSum / 2)
  let dp = new Array(totalSum+1).fill(false)
  dp[0] = true
  for (let curr of nums) {
    for (let idx=totalSum; idx >= curr-1; idx--) {
      dp[idx] = (dp[idx-curr] || dp[idx])
    }
  }
  return dp[totalSum]
  
};

console.log(canPartition([1,5,11,5]))
console.log(canPartition([2]))
