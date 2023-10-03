var twoOutOfThree = function(nums1, nums2, nums3) {
  // sol1 79ms 80% 44.3MB 81%
  let ans = new Set()
  for (let num of nums2) {
      if (nums1.indexOf(num) >= 0) {
          ans.add(num)
      }
  }
  for (let num of nums3) {
      if (nums1.indexOf(num) >= 0 || nums2.indexOf(num) >= 0) {
          ans.add(num)
      }
  }
  return [...ans]
};