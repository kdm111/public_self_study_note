var Solution = function(w) {
  // 1178ms 5%
  this.prefixSums = []
  let prefixSum = 0
  for (let weight of w) {
    prefixSum += weight
    this.prefixSums.push(prefixSum)
  }
  this.totalSum = prefixSum
};

Solution.prototype.pickIndex = function() {
  let target = this.totalSum * Math.random()
  for (let [idx, val] of this.prefixSums.entries()) {
    if (target < val) {
      return idx
    }
  }
};
let sol = new Solution([1,3])
