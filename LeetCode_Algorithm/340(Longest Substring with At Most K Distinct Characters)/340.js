var lengthOfLongestSubstringKDistinct = function(s, k) {
  // sol1 84ms 95%
  // O(n) O(k)
  // 
  if (s.length < k+1) {
    return s.length
  }
  let hashMap = new Map()
  left = right = ans = 0;
  while (right < s.length) {
    hashMap.set(s[right], right)
    if (hashMap.size == k+1) {
      let val = Math.min(...hashMap.values())
      hashMap.delete(s[val])
      left = val+1
    }
    ans = Math.max(ans, right-left+1)
    right += 1
  }  
  return ans
};
console.log(lengthOfLongestSubstringKDistinct("eceba", 2))