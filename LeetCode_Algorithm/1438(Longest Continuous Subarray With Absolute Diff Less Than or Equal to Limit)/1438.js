var longestSubarray = function(nums, limit) {
  // sol1 784ms 37% 60MB 5%
  let inc = []; let dec = []; let ans = 0
  let left = 0
  for (let [right, num] of nums.entries()) {
    while (inc && inc[inc.length-1] > num) {
      inc.pop()
    }
    while (dec && dec[dec.length-1] < num) {
      dec.pop()
    }
    inc.push(num)
    dec.push(num)
    while (dec[0] - inc[0] > limit) {
      if (inc[0] == nums[left]) {
        inc.shift()
      }
      if (dec[0] == nums[left]) {
        dec.shift()
      }
      left += 1
    }
    ans = Math.max(ans, right-left+1)
  }  
  return ans
};
console.log(longestSubarray([2,2,2,4,4,2,5,5,5,5,5,2], 2))