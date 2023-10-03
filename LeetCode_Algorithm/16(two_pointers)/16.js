var threeSumClosest = function(nums, target) {
  // sol2 two pointer 149ms 58%
  nums.sort((a, b) =>{return a-b})
  let ans = nums[0]+nums[1]+nums[2]
  for (let i=0; i < nums.length-2; i++) {
    let left = i+1; let right = nums.length-1
    while (left < right) {
      let temp = nums[i]+nums[left]+nums[right]
      if (Math.abs(target-temp) < Math.abs(target-ans)) {
        ans = temp
      } 
      if (temp < target) {
        left += 1
      } else {
        right -= 1
      }
    }
    if (ans == target) {
      break
    }
  }
  return ans
};

// console.log(threeSumClosest([-1,2,1,-4], 1))
console.log(threeSumClosest([0,1,2], 0))
