var sortedSquares = function(nums) {
  // sol1 O(n), O(n) 139~180ms 58~24%
  // stack = []
  // ans = []
  // for (let num of nums) {
  //   if (num < 0 ) {num *= -1}
  //   if (stack.length == 0 || stack[stack.length-1] >= num){
  //     stack.push(num); continue
  //   }
  //   while (stack.length > 0){
  //     if(stack[stack.length-1] < num){
  //       let n = stack.pop()    
  //       ans.push(n ** 2)
  //     }
  //     else{
  //       break
  //     }
  //   }
  //   stack.push(num)
  // }
  // while (stack.length >0 ){
  //   let n = stack.pop()
  //   ans.push(n ** 2)
  // }
  // return ans

  // sol2 O(n), O(1) 96~150ms 95~47% 
  var left = 0; var right = nums.length-1
  var idx = nums.length-1
  var ans = new Array(nums.length)

  while (0 <= idx){
    if (Math.abs(nums[left]) <= Math.abs(nums[right])){
      ans[idx] = nums[right]**2; right -= 1
    }
    else if (Math.abs(nums[left]) >Math.abs(nums[right])){
      ans[idx] = nums[left]**2; left += 1
    }
    idx -= 1
  }
  return ans
};
console.log(sortedSquares([-4,-1,0,3,10]))