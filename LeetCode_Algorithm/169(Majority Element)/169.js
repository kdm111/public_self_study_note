var majorityElement = function(nums) {
  // sol1 O(n^2), O(1) 시간초과
  // for (let num of nums){
  //   let cnt = 0
  //   for (let idx in nums){
  //     if(num == nums[idx]){
  //       cnt += 1
  //     }
  //   }
  //   if (cnt > parseInt(nums.length/2)){
  //     return num
  //   }
  // }

  // sol2 O(n), O(n) 98~130ms 47~14%
  // hashMap = {}
  // for (let num of nums){
  //   if (hashMap[num] == undefined) { hashMap[num] = 1 }
  //   else { hashMap[num] += 1 }
  // }
  // for (let key in hashMap) {
  //   if (hashMap[key] > parseInt(nums.length/2)){
  //     return key
  //   }
  // }

  // sol3 O(nlogn), O(1) 79~104ms 74~39%
  nums.sort(function(a,b){
    return a-b
  })
  return nums[parseInt(nums.length/2)]
  
};

console.log(majorityElement([1,2,2, 100]))