var merge = function(nums1, m, nums2, n) {
  // sol1 m+n 60~100ms 95~45%보다 빠름
  // var nums1Idx = m-1
  // var nums2Idx = n-1
  // for (let i = m+n-1; i >-1 ; i--){
  //   if (nums2Idx < 0){ break }
  //   if (nums1Idx >= 0 && nums2[nums2Idx] < nums1[nums1Idx]){
  //     nums1[i] = nums1[nums1Idx]
  //     nums1Idx -= 1
  //   }
  //   else{
  //     nums1[i] = nums2[nums2Idx]
  //     nums2Idx -= 1
  //   }
  // }

  // sol2 nlogn(https://stackoverflow.com/questions/57763205/what-is-array-prototype-sort-time-complexity)
  // 60~100ms 93~65%보다 빠름
  // js의 sort는 유니코드 순서대로 정렬하므로 1, 10, 2 숫자 순으로 정렬하는 것이 아니다.

  for (let i=0; i< n; i++){
    nums1[m+i] = nums2[i]
  }
  // sort의 파라미터를 사용하여 숫자 크기 순으로 정렬을 시도 
  nums1.sort(function(a,b){return a-b})
  console.log(nums1)

};

merge([1,2,3,0,0,0], 3, [2,5,6], 3)