var intersect = function(nums1, nums2) {
  // sol1 O(m+n), O(m or n) 60~68ms 97~86% 
  // hashMap = new Map()
  // for (let num of nums1) {
  //   if (!hashMap.has(num)){
  //     hashMap.set(num, 1)
  //   }
  //   else {
  //     hashMap.set(num, hashMap.get(num)+1)
  //   }
  // }
  // ans = new Array()
  // for (let num of nums2) {
  //   if (hashMap.has(num) && hashMap.get(num) > 0) {
  //     hashMap.set(num, hashMap.get(num)-1); ans.push(num)
  //   }
  // }
  // return ans

  // sol2 O(mlogm+nlogn) O(1) 98~105ms 36~27%
  nums1.sort(function (a,b) {return a-b}) 
  nums2.sort(function (a,b) {return a-b})

  nums1Idx = nums2Idx = 0;
  ans = new Array()
  while (nums1Idx < nums1.length && nums2Idx < nums2.length) {
    let num1 = nums1[nums1Idx]
    let num2 = nums2[nums2Idx]

    if (num1 < num2) {
      nums1Idx += 1
    }
    else if (num1 > num2) {
      nums2Idx += 1
    }
    else if (num1 == num2) {
      ans.push(num1);
      nums1Idx += 1; nums2Idx += 1
    }
  }
  return ans




};

console.log(intersect([10,2,2,1], [2,2]))