var removeDuplicates = function(nums) {
  //sol1 O(n), O(1) 92~100ms 73~65%
  var i = 0
  for (let j=1; j<nums.length; j++){
    if (nums[i] != nums[j]){
      i += 1; nums[i] = nums[j]
    }
  }
  console.log(nums)
  return i+1
};
console.log(removeDuplicates([1,2,2,3]))