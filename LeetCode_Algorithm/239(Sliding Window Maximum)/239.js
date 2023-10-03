var maxSlidingWindow = function(nums, k) {
  // sol2 1056ms 26%
  // O(n) O(n)
  if (nums.length == 0 || k == 0) {
    return []
  }
  if (k == 1) {
    return nums
  }
  let queue = []; let ans = []
  for (let [i,num] of nums.entries()) {
    while (queue.length > 0 && nums[queue[queue.length-1]] < num) {
      queue.pop()
    }
    queue.push(i)
    if (queue[0] == i-k) {
      queue.shift()
    }
    if (i > k-2) {
      ans.push(nums[queue[0]])
    }
  }
  return ans
};