var stringEqual = function(s, g) {
  let i = 0;
  while (i < s.length && i < g.length) {
    if (s[i] != g[i])
      return false;
    i++;
  }
  return i == s.length && i == g.length ? true : false
}

var rotateString = function(s, goal) {
  // sol1 66ms 89%
  let i = 0;
  while (i < s.length) {
    if (stringEqual(s,goal)) {
      return true
    }
    s = s.slice(1, ).concat(s.slice(0, 1))
    i++;
  }
  return false
};