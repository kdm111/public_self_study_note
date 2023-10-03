var largestAltitude = function(gain) {
  // sol1 49ms 93% 41.8MB 78%
  let ans = 0
  gain.reduce((acc, initVal) =>  {
    ans = Math.max(ans, acc+initVal)
    return acc+initVal
  }, 0)
  return ans
}
console.log(largestAltitude([52,-91,72]))