var intersection = function(nums1, nums2) {
  // sol1 O(mn), O(m+n) 432~512ms 5%
  // const ans = new Array()
  // for (let num1 of nums1){
  //   for (let num2 of nums2){
  //     if (ans.indexOf(num1) < 0 && num1 == num2){
  //       ans.push(num1)
  //     }
  //   }
  // }
  // return ans

  // sol2 O(m+n), O(n) 68~100ms 84~32%
  nums1.sort(function(a,b){ return a-b })
  nums2.sort(function(a,b){ return a-b })
  const ans = new Array()
  let nums1Idx = 0; let nums2Idx = 0
  while (nums1Idx < nums1.length && nums2Idx < nums2.length) {
    let num1 = nums1[nums1Idx]; let num2 = nums2[nums2Idx]
    if (ans.indexOf(num1) < 0 && num1 == num2){
      ans.push(num1)
      nums1Idx += 1
    }
    else if (nums1[nums1Idx] < nums2[nums2Idx]){
      nums1Idx += 1
    }
    else{
      nums2Idx += 1
    }
  }
  return ans
};
console.log(intersection([4,9,5], [9,4,9,8,4]))