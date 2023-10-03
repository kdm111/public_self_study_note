var findMedianSortedArrays = function(nums1, nums2) {
    // sol1 O(n) 224ms 20%
    let nums1Idx = 0; let nums2Idx = 0;
    mergedArr = []

    while (nums1Idx < nums1.length && nums2Idx < nums2.length){
      if (nums1[nums1Idx] < nums2[nums2Idx]) {
        mergedArr.push(nums1[nums1Idx])
        nums1Idx++;
      }
      else {
       mergedArr.push(nums2[nums2Idx])
       nums2Idx++   
      }
    }
    while (nums1Idx < nums1.length) {
      mergedArr.push(nums1[nums1Idx]); nums1Idx++;
    }

    while (nums2Idx < nums2.length){
      mergedArr.push(nums2[nums2Idx]); nums2Idx++;
    }


    const mid = parseInt(mergedArr.length / 2)
    if (mergedArr.length % 2 == 1) {
      return (mergedArr[mid])
    }
    else {
      return (mergedArr[mid] + mergedArr[mid-1]) / 2
    }


};

console.log(findMedianSortedArrays([1,2], [3,4]))