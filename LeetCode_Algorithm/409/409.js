var longestPalindrome = function(s) {

  // O(n) 145ms 5%
  let hashMap = {}
  for (let ch of s) {
    if (!hashMap[[ch]]) {
      hashMap[ch] = 1
    } else {
      hashMap[ch]++;
    }
  }
  let ans = 0;
  for (let key in hashMap) {
    ans += parseInt(hashMap[key] / 2) * 2
    if (ans % 2 == 0 && hashMap[key] % 2 == 1){
      ans += 1
    }
  }
  return ans
}

// console.log(longestPalindrome("aabba"))
console.log(longestPalindrome("abccccdd"))
