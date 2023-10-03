var findDifference = function(nums1, nums2) {
  // sol1 78ms 97% 49.1MB 33%
  let ans = [[], []]  
  let setNums1 = new Set(nums1)
  let setNums2 = new Set(nums2)
  setNums1.forEach((e) => {
    if (!setNums2.has(e)) {
      ans[0].push(e)
    }
  })
  setNums2.forEach((e) => {
    if (!setNums1.has(e)) {
      ans[1].push(e)
    }
  })
  return ans
};

console.log(findDifference([1,2,3],[2,4,6]))