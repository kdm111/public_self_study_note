var maxProduct = function(nums) {
  // sol2 94ms 53%
  if (!nums) {return 0}
  let ans = nums[0]
  let maxV = nums[0]; let minV = nums[0]

  for (let curr of nums.slice(1,)){
    let temp = Math.max(curr, maxV*curr, minV*curr)
    minV = Math.min(curr, maxV*curr, minV*curr)
    maxV = temp
    ans = Math.max(ans, maxV)
  }
  return ans
};

console.log(maxProduct([-2,-3,-4]))