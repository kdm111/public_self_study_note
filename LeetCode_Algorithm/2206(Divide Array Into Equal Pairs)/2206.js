var divideArray = function(nums) {
  // sol2 54ms 100% 43.5MB 97%
  let hashSet = new Set()
  for (let num of nums) {
    if (hashSet.has(num)) {
      hashSet.delete(num)
    } else {
      hashSet.add(num)
    }
  }  
  return hashSet.size == 0
};