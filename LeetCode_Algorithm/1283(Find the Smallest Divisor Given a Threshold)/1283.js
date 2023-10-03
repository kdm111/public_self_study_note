var smallestDivisor = function(nums, threshold) {
  // sol1 83ms 53% 46.3MB 36%
  let l = 1; let r = Math.max(...nums)  
  while (l < r) {
    let m = Math.floor((l + r) / 2)
    if (solve(nums, m) > threshold) 
      l = m + 1
    else
      r = m
  }
  return l
};

var solve = (nums, m) => {
  let ret = 0
  for (let num of nums) {
    ret += Math.ceil(num / m)
  }
  return ret
}