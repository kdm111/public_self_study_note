var productExceptSelf = function(nums) {
  // sol1 87ms 99% 52.3MB 96%
  let totalProduct = 1; let zeroCnt = 0
  for (let num of nums) {
    if (num == 0) {
      zeroCnt += 1; continue
    }
    totalProduct *= num
  }
  for (let i = 0; i < nums.length; i++) {
    if (nums[i] == 0) {
      nums[i] = zeroCnt == 0 ? totalProduct : 0
    }
    else {
      nums[i] = zeroCnt == 0 ? parseInt(totalProduct / nums[i]) : 0
    }
  }
  return nums
};