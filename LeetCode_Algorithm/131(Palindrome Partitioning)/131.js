var isPalindrome = (s) => {
  for (let i=0; i < parseInt(s.length / 2); i++) {
    if (s[i] != s[s.length-1-i])
      return false
  }
  return true
}

var solve = (s, temp) => {
  if (!s)
    ans.push(temp.slice(0, ));
  for (let i=1;i < s.length+1; i++) {
    if (isPalindrome(s.slice(0,i))) {
      temp.push(s.slice(0, i))
      solve(s.slice(i,), temp)
      temp.pop()
    }
  }
}

var partition = function(s) {
  // sol1 250ms 89% 63.3MB 75%
  ans = []
  solve(s, [])
  return ans
};
console.log(partition("aab"))