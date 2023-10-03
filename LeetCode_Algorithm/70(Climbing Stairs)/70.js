var climbStairs = function(n) {
  // sol1 n^2 44에서 시간초과
  // if (n==1) { return 1 }
  // if (n==2) { return 2 }
  
  // return cnt(n)

  // sol2 85~110ms 45~10%보다 빠름
  // var memory = {}
  // memory[0] = 0
  // memory[1] = 1
  // memory[2] = 2
  
  // return cnt2(n, memory)

  // sol3 77~109ms 58~14%보다 빠름
  // memoization
  // 메모리가 O(n)인 솔루션

  // var nums = Array.from({length : 46}, (v) => 0)

  // nums[1] = 1
  // nums[2] = 2
  
  // for (let idx=3; idx < n+1; idx++){
  //   nums[idx] = nums[idx-1]+nums[idx-2]
  // }
  // return nums[n]

  // sol4 56~95 96~30%보다 빠름
  // 메모리가 O(1)

  // var first = 1  
  // var second = 2
  // if (n==1) {return 1}
  // if (n==2) {return 2}

  // for (let i=3; i < n+1; i++){
  //   var third = first+second
  //   first = second
  //   second = third
  // }
  // return third

  // sol5 60ms 51% 41.6MB 70%
  if (dp[n] > 0)
    return dp[n]
  dp[n] = climbStairs(n - 2) + climbStairs(n - 1)
  return dp[n]
};
var dp = new Array(46).fill(0)
dp[0] = 1; dp[1] = 1; dp[2] = 2
// function cnt(n){
//   if (n<=1){return 1}
//   return cnt(n-2)+cnt(n-1)
// }
function cnt2(n, memory){

  if (memory[n] != undefined){
    return memory[n]
  }
  if (n > 2){
    let ways = cnt2(n-2, memory)+cnt2(n-1, memory)
    memory[n] = ways
    return ways
  }

}
console.log(climbStairs(44))