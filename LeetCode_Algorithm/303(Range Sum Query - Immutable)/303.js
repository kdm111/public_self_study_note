var NumArray = function(nums) {
  // sol2 89ms 81% 48.87MB 60%
  // this.prefixSum = [0];
  // for (let num of nums) {
  //   this.prefixSum.push(this.prefixSum[this.prefixSum.length - 1] + num)  
  // }

  // sol2-2 92ms 75% 48.59MB 79%
  this.prefixSum = [0];
  nums.reduce((acc, init) => {
    this.prefixSum.push(acc + init)
    return acc + init  
  }, 0)
};

NumArray.prototype.sumRange = function(left, right) {
  return this.prefixSum[right+1] - this.prefixSum[left]
};
