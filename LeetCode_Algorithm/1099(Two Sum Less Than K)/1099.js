var twoSumLessThanK = function(nums, k) {
  // sol2 61ms 97% 44.1MB 10%
  let ans = -1
  let cntArr = new Array(1001).fill(0)
  for (let num of nums) {
    cntArr[num] += 1
  }
  let left = 0; let right = cntArr.length-1
  while (left <= right) {
    if (left + right >= k || cntArr[right] == 0) {
      right -= 1
    } else {
      if (cntArr[left] > (left < right ? 0 : 1)) {
        ans = Math.max(left+right, ans)
      }
      left += 1
    }
  }
  return ans
};

console.log(twoSumLessThanK([34,23,1,24,75,33,54,8], 60))