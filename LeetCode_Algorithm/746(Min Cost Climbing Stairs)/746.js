var minCostClimbingStairs = function(cost) {
  // O(n), O(1) 127ms 12%
  // if (cost.length == 2){
  //   return Math.min(cost[0], cost[1])
  // }
  // let dp = [cost[0], cost[1]]
  // for (let i=2; i < cost.length; i++) {
  //   dp.push(Math.min(dp[i-2]+cost[i], dp[i-1]+cost[i]))
  // }
  // return Math.min(dp[dp.length-2], dp[dp.length-1])

  // O(n), O(1) 116ms 21%
  var one = 0; var two = 0
  for (let i = 2; i < cost.length+1; i++) {
    let temp = one
    one = Math.min(one + cost[i-1], two + cost[i-2])
    two = temp
  }
  return one
};