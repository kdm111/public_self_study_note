var checkInclusion = function(s1, s2) {
  // sol2 224ms 38%
  let hashMap = new Map()  
  for (let c of s1) {
    if (c in hashMap) {
      hashMap[c] += 1
    } else{
      hashMap[c] = 1
    }
  }

  for (let i=0; i < s2.length; i++) {
    if (s2[i] in hashMap){
      hashMap[s2[i]] -= 1
    }
    if (i >= s1.length && s2[i-s1.length] in hashMap){
      hashMap[s2[i-s1.length]] += 1
    }
    if (check(hashMap)) {
      return true
    }
  }
  return false
};
var check = function(hashMap) {
  for (const k in hashMap) {
    if (hashMap[k] != 0) {
      return false
    }
  }
  return true
}

console.log(checkInclusion("ccc", "cbac"))