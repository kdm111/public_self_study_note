var answerQueries = function(nums, queries) {
  //sol2 75ms 94% 45.2MB 48%
  let prefixSum = Array(nums.length); let temp = 0
  for (let i = 0; i < nums.length; i++) {
    temp += nums[i]
    prefixSum[i] = temp
  }
  let ans = Array()
  for (let i = 0; i < queries.length; i++) {
    if (queries[i] < prefixSum[0]) {
      ans.push(0)
    } else {
      ans.push(-1)
      let l = 0; let r = prefixSum.length - 1
      while (l <= r) {
        let m = Math.floor((l+r) / 2)
        if (queries[i] == prefixSum[m]) {
          ans[ans.length-1] = m + 1
          break
        } else if (queries[i] < prefixSum[m]) {
          r = m - 1
        } else {
          l = m + 1
        }
      }
      if (l > r) 
        ans[ans.length-1] = r + 1
    }
  }
  return ans
};