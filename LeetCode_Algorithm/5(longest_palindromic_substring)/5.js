var check = function(s, start, end) {
  while (-1 < start && end < s.length && s[start] == s[end]) {
    start -= 1
    end += 1
  }
  return s.slice(start+1, end)
}
var longestPalindrome = function(s) {
  // sol1 O(n^2) 100ms 95% 
  let ans = ""
  for (let i in s) {
    let n = parseInt(i)
    let temp1 = check(s, n, n)
    let temp2 = check(s, n, n+1)
    if (ans.length < temp1.length) {ans = temp1}
    if (ans.length < temp2.length) {ans = temp2}
  }
  return ans
};


console.log(longestPalindrome("bbbbb"))