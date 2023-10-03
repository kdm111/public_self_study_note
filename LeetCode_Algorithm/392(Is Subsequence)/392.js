var isSubsequence = function(s, t) {
  // sol1 O(t), O(1) 60~89ms 94~37%
  var sIdx = 0; var tIdx = 0;
  while (sIdx < s.length && tIdx < t.length) {
    if (s[sIdx] == t[tIdx]) {
      sIdx += 1; tIdx += 1; 
      continue 
    }
    tIdx += 1
  }
  return (sIdx == s.length)
};
console.log(isSubsequence("abc", "acbac"))