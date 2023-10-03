var arrayPairSum = function(nums) {
  // sol1 252ms 11% 50.5MB 8%
  nums.sort((a,b) => {return a-b})
  let idx = 0; let ans = 0;
  console.log(nums)
  while (idx < nums.length) {
    ans += nums[idx]
    idx += 2
  }
  return ans
};

console.log(arrayPairSum([6214, -2290, 2833, -7908]))