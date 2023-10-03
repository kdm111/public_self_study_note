var findErrorNums = function(nums) {
  // sol2 T : 112ms 76.6% S : 45MB 81%

  let dup = -1; 
  for (let num of nums) {
    if (nums[Math.abs(num)-1] < 0) {
      dup = Math.abs(num)
    }
    else {
      nums[Math.abs(num)-1] *= -1
    }
  }
  let missing = 1;
  for (let i = 1; i < nums.length; i++) {
    if (nums[i] > 0) {
      missing = i + 1
    }
  }
  return [dup, missing]
};
console.log(findErrorNums([1,2,2,4]))