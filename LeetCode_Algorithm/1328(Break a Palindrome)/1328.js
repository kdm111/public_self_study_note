var breakPalindrome = function(palindrome) {
  // sol1 64ms 89% 43.6MB 7%
  if (palindrome.length == 1) {
    return ""
  }  
  palindrome = Array(...palindrome)
  for (let i=0; i < parseInt(palindrome.length / 2); i++) {
    if (palindrome[i] != 'a') {
      palindrome[i] = 'a';
      return palindrome.join("")
    }
  }
  palindrome[palindrome.length-1] = 'b'
  return palindrome.join("")
};