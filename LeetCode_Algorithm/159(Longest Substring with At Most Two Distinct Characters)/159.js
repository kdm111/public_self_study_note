var lengthOfLongestSubstringTwoDistinct = function(s) {
  // sol1 447ms 29%
  let ans = left = right = 0
  let hashMap = new Map()
  while (right < s.length) {
    hashMap.set(s[right], right)
    if (hashMap.size == 3) {
      let val = Math.min(...hashMap.values())
      hashMap.delete(s[val])
      left = val+1
    }
    ans = Math.max(ans, right-left+1)
    right += 1
  }
  return ans

};
console.log(lengthOfLongestSubstringTwoDistinct("ebeac"))