var findDisappearedNumbers = function(nums) {

  // sol2 O(n), O(n) 160~248ms 44~22%
  // sol3 보다 17~25MB 더 사용
  hashMap = new Map()

  for (let num of nums) {
    if (hashMap.has(num) == false){
      hashMap.set(num,1)
    }
  }
  console.log(hashMap)
  ans = new Array()
  for (let num=1; num<nums.length+1; num++){
    if (hashMap.has(num) == false){
      ans.push(num)
    }
  }
  return ans

  // sol3 O(n), O(1) 119~148ms 77~53%
  // for (let num of nums){
  //   const newIdx = Math.abs(num)-1
  //   if (nums[newIdx] > 0) {
  //     nums[newIdx] *= -1
  //   }
  // }


  // var ans = []
  // for (let idx=1; idx<nums.length+1; idx++){
  //   if (nums[idx-1] > 0){
  //     ans.push(idx)
  //   }
  // }
  // return ans
};
console.log(findDisappearedNumbers([4,3,2,7,8,2,3,1]))