var engCnter = () => {
  hashMap = {}
  for (let i = 97; i < 123; i++) {
    hashMap[String.fromCharCode(i)] = 0
  }
  return hashMap
}
var canPermutePalindrome = function(s) {
  // sol1 92ms 42% 42MB 41%
  let hashMap = engCnter()
  for (let c of s) {
    hashMap[c] += 1
  }
  oddCnt = 0
  for (let k of hashMap) {
    if (hashMap[k] % 2 == 1)
      oddCnt += 1
    if (oddCnt < 2)
      return false
  }
  return oddCnt < 2
};
console.log(canPermutePalindrome("aa"))