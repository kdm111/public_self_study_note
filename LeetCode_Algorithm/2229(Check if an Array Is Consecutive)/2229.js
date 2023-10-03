var isConsecutive = function(nums) {
  // sol1 168ms 76% 63.2MB 12%
  let size = nums.length; let i = 0; let num = Math.min(...nums)
  nums = new Set(nums)
  while (i < size) {
    if (!nums.has(num+i)) {
      return false
    }
    i += 1
  }
  return true
  // sol2 95ms 100% 61MB 16%
  return (Math.max(...nums) - Math.min(...nums) + 1) == nums.length && nums.length == new Set(nums).size
};