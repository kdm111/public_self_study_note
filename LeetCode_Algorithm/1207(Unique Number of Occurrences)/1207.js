var uniqueOccurrences = function(arr) {
  // sol1 92ms 63% 43.6MB 24%
  let hashMap = {}
  for (let num of arr) {
    if (hashMap[num] != undefined) {
      hashMap[num] += 1
    } else {
      hashMap[num] = 1
    }
  }
  cntMap = {}
  for (let [k,v] of Object.entries(hashMap)) {
    if (cntMap[v] != undefined) {
      return false
    }
    cntMap[v] = k
  }
  return true
};

console.log(uniqueOccurrences([1,1,1,2,2,3,3]))