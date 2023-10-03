var candy = function(ratings) {
  // sol1 하나밖에 없음 78ms 41% 46.4MB 23%
  let n = ratings.length
  let left = Array(n).fill(1)
  let right = Array(n).fill(1)
  for (let i = 1; i < n; i++) {
    if (ratings[i] > ratings[i-1]) {
      left[i] = left[i-1] + 1
    }
  }
  for (let i = n-2; i >= 0; i--) {
    if (ratings[i] > ratings[i+1]) {
      right[i] = right[i+1] + 1
    }
  }
  let ans = 0
  for (let i = 0; i < n; i++) {
    ans += Math.max(left[i], right[i])
  }
  return ans
};
