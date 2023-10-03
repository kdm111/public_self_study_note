var minWindow = function(s, t) {
  // sol2 97ms 90%
  let hashMap = new Map()
  for (let c of t) {
    if (hashMap[c] == undefined) {
      hashMap[c] = 1
    } else{
      hashMap[c] += 1
    }
  }
  let ans = ""; let tCounting = t.length
  let left = 0; let right = 0;
  while (right < s.length) {
    if (hashMap[s[right]] != undefined) {
      hashMap[s[right]] -= 1
      if (hashMap[s[right]] > 0 || hashMap[s[right]] == 0) {
        tCounting -= 1
      }
    }
    while (tCounting == 0) {

      let temp = s.slice(left,right+1)
      if (ans == "" || ans.length > temp.length) {
        ans = temp
      }
      if (hashMap[s[left]] != undefined) {
        hashMap[s[left]] += 1
        if (hashMap[s[left]] > 0){
          tCounting += 1
        }
      }
      left += 1
    }
    right += 1
  }
  return ans
};

console.log(minWindow("ADOBECODEBANC", "ABC"))