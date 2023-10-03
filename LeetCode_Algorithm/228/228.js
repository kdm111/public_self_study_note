var summaryRanges = function(nums) {
  
  // sol1 O(n), O(1) 75~96ms 53~17%
  var ans = new Array()
  var i = 0

  for (j=0; j<nums.length;j++){
    if(j+1 < nums.length && nums[j+1] == nums[j]+1){
      continue
    }
    else{
      if(i==j){
        ans.push(String(nums[j]))
      }
      else{
        ans.push(nums[i]+"->"+nums[j])
      }
      i = j+1
    }
  }
  return ans
};

console.log(summaryRanges([0,2,3,4,6,8,9]))