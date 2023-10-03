var findPeakElement = function(nums) {
 // sol1 55ms 74% 42.3MB 30%
 let l = 0; let r = nums.length
 while (l < r) {
  let m1 = parseInt((l + r) / 2)
  let m2 = m1 + 1
  if (nums[m1] < nums[m2]) {
    l = m1 + 1
  } else {
    r = m1
  }
 }   
 return l
}