var numFactoredBinaryTrees = function(arr) {
  // 127ms 97% 44.6MB 94%
  let dp = Array(arr.length).fill(1)
  let mod = 10 ** 9 + 7
  arr.sort((a,b) => {return a-b})
  let idx = new Set(arr)
  for (let i = 0; i < arr.length; i++) {
    for (let j = 0; j < i; j++) {
      if (arr[i] % arr[j] == 0) {
        let right = parseInt(arr[i] / arr[j])
        if (idx.has(right)) {
          dp[i] += dp[j] * dp[arr.indexOf(right)]
          dp[i] %= mod
        }
      }
    }
  }
  return (dp.reduce((a,b) => a+b, 0) % mod)
};