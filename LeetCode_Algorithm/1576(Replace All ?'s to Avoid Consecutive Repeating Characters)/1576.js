var modifyString = function(s) {
  // sol1 80ms 83% 44.3M 18%
  s = new Array(...s)
  for (let i=0; i < s.length; i++) {
    if (s[i] == '?') {
      for (let c of "abc") {
        if (i-1 >= 0 && s[i-1] == c) {continue}
        if (i+1 < s.length && s[i+1] == c) {continue}
        s[i] = c; break
      }
    }
  }
  return s.join("")
};
