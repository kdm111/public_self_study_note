var isPalindrome = function(s) {
  let left = 0; let right = s.length-1
  while (left < right) {
    if (s[left] != s[right]) {
      return false
    }
    left += 1; right -= 1
  }
  return true
}
var removePalindromeSub = function(s) {
  // sol1 75ms 81% 42.7MB 5.4%
  return 2 - (s == s.split('').reverse().join('')) - (s == '')
  // sol2 81ms 75% 42.4MB 7%
  if (s == '')
    return 0
  return 2 - isPalindrome(s)
};