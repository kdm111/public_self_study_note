var solve = function(idx, s) {
  let ret = []
  for (let i = idx; i < s.length; i++) {
    if (ret.includes(s[i]) == false) {
      ret.push(s[i])
    } else {
      break
    }
  }
  return ret.join("")
}

var lengthOfLongestSubstring = function(s) {
  // sol2 O(2n) O(n) 1878ms 5%
  let ans = ""
  for (let idx in s) {
    let temp = solve(idx, s)
    if (ans.length < temp.length) {
      ans = temp
    }
  }
  return ans.length
};

// console.log(lengthOfLongestSubstring("bbbbb"))
console.log(lengthOfLongestSubstring("pwwkew"))
