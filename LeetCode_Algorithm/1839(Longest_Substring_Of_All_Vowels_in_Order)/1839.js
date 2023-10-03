var longestBeautifulSubstring = function(word) {
  // sol2 144ms 75% 53.6MB 13%
  let seen = new Set()
  let left = 0; let right = 0; let ans = 0
  while (right < word.length) {
    if (right > 0 && word[right-1] > word[right]) {
      seen = new Set()
      left = right
    }
    seen.add(word[right])
    right += 1
    if (seen.size == 5)
      ans = Math.max(ans, right-left)
  }
  return ans
};

console.log(longestBeautifulSubstring("aeiaaioaaaaeiiiiouuuooaauuaeiu"))