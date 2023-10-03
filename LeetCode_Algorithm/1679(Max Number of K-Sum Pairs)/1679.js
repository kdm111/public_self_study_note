var maxOperations = function(nums, k) {
  // sol1 104ms 93% 57.1MB 35%
  counter = new Map()
  for (let num of nums) {
    counter.set(num, (counter.get(num) || 0)+1)
  }
  ans = 0
  for (let key of counter.keys()) {
    if (counter.has(k-key)) {
      ans += Math.min(counter.get(k-key), counter.get(key))
    }
  }
  return parseInt(ans / 2)
};
console.log(maxOperations([1,2,3,4,5], 5))