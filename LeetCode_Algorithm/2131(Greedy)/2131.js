var longestPalindrome = function(words) {
  // sol1 O(n) O(n) 745ms 5%
  var hashMap = {}; let ans = 0; let temp = 0

  for (let word of words) {
    const r_word = word.split("").reverse().join("")
    if (word[0] != word[1]) {
      if (hashMap[r_word] > 0) {
        hashMap[r_word] -= 1; ans += 4
      } else if (hashMap[word] == undefined) {
        hashMap[word] = 1
      } else {
        hashMap[word] += 1
      }
    }
    else {
      if (hashMap[word] > 0) {
        hashMap[word] -= 1; ans += 4; temp -= 1
      } else if (hashMap[word] == undefined) {
        hashMap[word] = 1; temp +=1
      } else {
        hashMap[word] += 1; temp += 1
      }
    }
  }
  if (temp > 0) {ans += 2}
  return ans

};

console.log(longestPalindrome(["lc","cl","gg"]))

