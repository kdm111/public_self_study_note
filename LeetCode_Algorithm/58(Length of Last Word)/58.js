var lengthOfLastWord = function(s) {
  // sol1 trim
  // 66ms 16% 41.7MB 76%
  // s = s.trim(); ans = 0
  // for (let i = s.length -1; i >= 0; i--) {
  //   if (s[i] == ' ') {
  //     break
  //   } else {
  //     ans += 1
  //   }
  // } 
  // return ans

  // sol2 59ms 53% 41.3MB 97%
  let ans = 0; let i = s.length-1
  while (i >= 0 && s[i] == ' ') {
    i--;
  }
  while (i >= 0 && s[i] != ' ') {
    ans++; i--;
  }
  return ans
};

console.log(lengthOfLastWord("   fly me   to   the moon  "))