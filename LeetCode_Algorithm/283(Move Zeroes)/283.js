var moveZeroes = function(nums) {
  // sol1 O(n), O(n) 86~171ms 94~20%
  // var temp = []
  // for (let num of nums){
  //   if (num != 0) {
  //     temp.push(num)
  //   }
  // }

  // i = nums.length - temp.length
  // while (i > 0){
  //   temp.push(0)
  //   i -= 1
  // }
  
  // for (let i=0; i < nums.length; i++){
  //   nums[i] = temp[i]
  // }

  // sol2 O(n), O(1) 123~156ms 59~29%
  var idx0 = -1
  for (let idx=0; idx < nums.length; idx++){
    if (nums[idx] == 0){
      idx0 = idx; break;
    }
  }

  if(idx0 < 0){
    return
  }

  for (let idx=idx0+1; idx < nums.length; idx++){
    if (nums[idx] != 0) {
      let temp = nums[idx0]
      nums[idx0] = nums[idx]; 
      nums[idx] = temp;  
      while (idx0 < nums.length) {
        idx0 += 1
        if (nums[idx0] == 0){
          break;
        }
      }
    }
  }

  // sol3
  var swap = (left, right) => {
    let temp = nums[left]
    nums[left] = nums[right]
    nums[right] = temp
  }
  let left = 0
  for (let right = 0; right < nums.length; right++) {
    if (nums[right] != 0) {
      if (nums[left] != nums[right]) {
        swap(left, right)
      }
      left += 1
    }
  }

};

moveZeroes([0,1,0,3,12])