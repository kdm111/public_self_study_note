var validPalindrome = function(s) {
    
  // sol1 O(n), O(1) 104~160ms 65~15%

  var i = 0; var j = s.length-1

  while (i < j) {
    if (s[i] != s[j]) {
      return checkPalindrome(s, i+1, j) || checkPalindrome(s, i, j-1)
    }
    i += 1
    j -= 1
  }
  return true
};
var checkPalindrome = function(s, i, j) {
  while (i < j) {
    if (s[i] != s[j]){
      return false
    }
    i += 1
    j -= 1
  }
  return true
}

console.log(validPalindrome("abab"))