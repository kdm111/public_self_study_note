var containsDuplicate = function(nums) {
    
  // sol1 n^2 1500~2500ms 11%~4% 보다 빠름
  // for (let i=0; i < nums.length; i++){
  //   for (let j=i+1; j < nums.length; j++){
  //     if (nums[i] == nums[j]){return true}
  //   }
  // }
  // return false

  // sol2 nlogn 280~300ms 20%~16%보다 빠름
  // nums.sort()
  // for (let i=0; i < nums.length-1; i++){
  //   if(nums[i]==nums[i+1]) { return true }
  // }
  // return false

  // sol3 n 84~96ms 95~85%보다 빠름
  const map = {}
  for (let i=0; i < nums.length; i++){
    if ( map[nums[i]]){ return true}
    else{map[nums[i]] = 1}
  }
  return false


};

console.log(containsDuplicate([1,2,3,4,1]))
console.log(containsDuplicate([1,2,3,4]))
