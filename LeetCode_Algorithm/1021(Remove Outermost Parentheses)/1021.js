var removeOuterParentheses = function(s) {
  // sol1 55ms 82% 42MB 98%
  let cnt = 0; let l = 0; let ans = ""
  for (let r = 0; r < s.length; r++) {
    s[r] == '(' ? cnt += 1 : cnt -= 1
    if (cnt == 0) {
      ans += s.slice(l+1, r)
      l = r + 1
    }
  }  
  return ans
};
console.log(removeOuterParentheses("(()())(())"))