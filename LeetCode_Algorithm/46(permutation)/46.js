var permute = function(nums) {
  // sol1 108ms 54%
  let ans = []
  var backtracking = function(n) {
    if (n == nums.length) {
      ans.push(nums.slice())
    } 
    for (let i=n; i<nums.length; i++) {
      let temp = nums[i]; nums[i] = nums[n]; nums[n] = temp
      backtracking(n+1)
      temp = nums[i]; nums[i] = nums[n]; nums[n] = temp
    }
  }
  backtracking(0)
  return ans
};

console.log(permute([1,2,3]))