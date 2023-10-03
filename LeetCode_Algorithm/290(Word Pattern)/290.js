var wordPattern = function(pattern, s) {
  // sol2 67ms 74% 42.2MB 25%
  if (pattern.length != s.split(" ").length) {
    return false
  }
  s = s.split(" ")
  let wordHashMap = {}; let patternHashMap = {}
  for (let i=0; i < pattern.length; i++) {
    if (!patternHashMap[pattern[i]] && !wordHashMap[s[i]]) {
      wordHashMap[s[i]] = pattern[i]; patternHashMap[pattern[i]] = s[i]
    } else {
      if (wordHashMap[s[i]] != pattern[i] || patternHashMap[pattern[i]] != s[i])
        return false
    }
  }
  console.log(wordHashMap, patternHashMap)
  return true
};
console.log(wordPattern("abc", "dog cat dog"))