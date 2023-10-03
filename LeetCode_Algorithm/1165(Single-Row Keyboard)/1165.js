var calculateTime = function(keyboard, word) {
  // sol1 70ms 95% 43.7MB 38%
  let hashMap = {}
  for (let i=0; i < keyboard.length; i++) {
    hashMap[keyboard[i]] = i
  }  
  let ans = curr = 0
  for (let c of word) {
    ans += Math.abs(hashMap[c] - curr)
    curr = hashMap[c]
  }
  return ans
};