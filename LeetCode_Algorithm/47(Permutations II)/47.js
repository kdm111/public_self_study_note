var solve = function(path, counter, length) {
  if (path.length == length) {
    ans.push(path); return ;
  }
  counter.forEach((_,k) => {
    if (counter.get(k) > 0) {
      counter.set(k, counter.get(k)-1)
      path.push(k)
      solve([...path], counter, length)
      path.pop()
      counter.set(k, counter.get(k)+1)
    }
  })
}
var permuteUnique = function(nums) {
  // sol1 T : 79ms 96% S : 45.6MB 56.4%
  let hashMap = new Map()
  for (let num of nums) {
    if (hashMap.has(num)) {
      hashMap.set(num, hashMap.get(num)+1)
    } else {
      hashMap.set(num, 1)
    }
  }
  let path = []; ans = []
  solve(path, hashMap, nums.length)
  return ans
};

console.log(permuteUnique([1,2,2]))