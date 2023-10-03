var totalFruit = function(fruits) {
  // sol1 111ms 89% 53.7MB 64%
  let hashMap = new Map(); let i = 0; let j = 0;
  let ans = 0
  while (j < fruits.length) {
    if (hashMap.has(fruits[j])) {
      hashMap.set(fruits[j], hashMap.get(fruits[j])+1)
    } else {
      hashMap.set(fruits[j], 1)
    }
    while (hashMap.size > 2) {
      hashMap.set(fruits[i], hashMap.get(fruits[i])-1)
      if (hashMap.get(fruits[i]) == 0) {
        hashMap.delete(fruits[i])
      }
      i += 1
    }
    j += 1
    ans = Math.max(ans, j-i)
  }
  return ans
};

console.log(totalFruit([1,2,2,3,3,3,1]))