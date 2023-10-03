var equalSubstring = function(s, t, maxCost) {
  // sol1 58ms 62% 43.52MB 23.23%
  let i = j = ans = 0
  while (j < t.length) {
    maxCost -= Math.abs(t[j].charCodeAt(0) - s[j].charCodeAt(0))
    while (maxCost < 0) {
      maxCost += Math.abs(t[i].charCodeAt(0) - s[i].charCodeAt(0))
      i += 1
    }
    j += 1
    ans = Math.max(ans, j - i)
  }
  return ans
};


console.log(equalSubstring("abcd", "bcdf", 3))