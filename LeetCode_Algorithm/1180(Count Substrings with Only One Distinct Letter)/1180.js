var countLetters = function(s) {
  // sol1 66ms 92%  42.3MB 65%
  let ans = 1; let cnt = 1
  for (let i=1; i < s.length; i++) {
    if (s[i-1] != s[i]) {
      cnt = 1
    } else {
      cnt += 1
    }
    ans += cnt
  }  
  return ans
};