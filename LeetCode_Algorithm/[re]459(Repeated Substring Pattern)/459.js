var repeatedSubstringPattern = function(s) {
  // sol2 67ms 72% 46.7MB 61%
  let prefix = kmp(s)
  let n = prefix[s.length-1]
  return n != 0 && s.length %(s.length - n) == 0
  
};
var kmp = function(s) {
  let i = 0; let j = 1; 
  let kmp = new Array(s.length).fill(0)
  while (i < s.length && j < s.length) {
    if (s[i] == s[j]) {
      kmp[j] = i + 1
      j += 1
      i += 1
    } else {
      if (i == 0) {
        kmp[j] = 0
        j += 1
      } else{
        i = kmp[i - 1]
      }
    }
  }
  return kmp
}

console.log(repeatedSubstringPattern("abab"))