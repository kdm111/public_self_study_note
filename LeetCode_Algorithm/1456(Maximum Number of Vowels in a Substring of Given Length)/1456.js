var maxVowels = function(s, k) {
  // sol1 78ms 66.5% 45.6MB 59%
  let ans = 0; const counter = new Set(['a','e','i','o','u'])
  for (let i =0 ; i < k; i++) {
      if (counter.has(s[i]))
          ans += 1
  }
  let temp = ans
  for (let i = k; i < s.length; i++) {
      if (counter.has(s[i]))
          temp += 1
      if (counter.has(s[i-k]))
          temp -= 1
      ans = Math.max(temp, ans)
  }
  return ans
};