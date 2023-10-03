var containsNearbyDuplicate = function(nums, k) {
  // sol1 O(n), O(n) 275~392 20~15%
  // const hashMap = new Map()
  // for (const [idx, num] of nums.entries()) {
  //   if (hashMap.has(num)) {
  //     if (idx-hashMap.get(num)<=k) {
  //       return true
  //     }
  //   }
  //   hashMap.set(num ,idx)
  // }
  // return false


  // sol2 O(n * min(k,n)) O(1) 1832~2426ms 12~10%
  for (let i=0; i<nums.length; i++){
    var j = i+1
    while (j < nums.length){
      if (i+k < j) {break;}
      if (nums[i] == nums[j]) {return true}
      j += 1
    }
  }
  return false
};
console.log(containsNearbyDuplicate([1,2,3,1,1,2,3], 0))
console.log(containsNearbyDuplicate([1,2,3,1], 3))
