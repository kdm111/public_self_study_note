var swap = function(nums, i, j){
  let temp = nums[i]
  nums[i] = nums[j]
  nums[j] = temp
}
var reverse = function(nums, left, right) {
  while (left < right) {
    swap(nums,left, right)
    left += 1; right -= 1;
  }
}
var nextPermutation = function(nums) {
  let i = nums.length-2
  while (i > -1 && (nums[i] < nums[i+1] || nums[i] == nums[i+1])) {
    i--;
  }
  if (i > -1) {
    let j = nums.length-1
    while (j > i && (nums[j] < nums[i] || nums[i] == nums[j])) {
      j--;
    }
    swap(nums,i,j)
  }
  reverse(nums, i+1, nums.length-1)
  return nums
  
};
console.log(nextPermutation([1,3,2]))
console.log(nextPermutation([1,2,3]))
