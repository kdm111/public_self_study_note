var longestCommonPrefix = function(strs) {
  
  // sol1 T : 73ms 90% S : 42.8MB 46%
  let ans = strs.length > 0 ? strs[0] : ""
  for (let i = 1; i < strs.length; i++) {
    let charIdx = 0; let minLen = Math.min(strs[i].length, ans.length)
    while (charIdx < minLen) {
      if (ans[charIdx] != strs[i][charIdx]) {
        break ;
      }
      charIdx += 1
    }
    ans = ans.slice(0, charIdx)
  }
  return ans

};

console.log(longestCommonPrefix(["flower","flow","flight"]))
console.log(longestCommonPrefix(["dog"]))
