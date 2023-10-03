var trap = function(height) {
  // sol1 100ms 53%
  // const leftArr = new Array(height.length).fill(0); let leftMax = height[0]
  // const rightArr = new Array(height.length).fill(0); let rightMax = height[height.length-1]
  
  // var idx = 0
  // while (idx < leftArr.length) {
  //   if (leftMax > height[idx]) {
  //     leftArr[idx] = leftMax-height[idx]
  //   }
  //   else if (leftMax < height[idx]) {
  //     leftMax = height[idx]
  //   }
  //   idx++
  // }

  // var idx = height.length-1
  // while (idx >= 0) {
  //   if (rightMax > height[idx]) {
  //     rightArr[idx] = rightMax-height[idx]
  //   }
  //   else if (rightMax < height[idx]) {
  //     rightMax = height[idx]
  //   }
  //   idx--;
  // }

  // let ans = 0
  // for (let i=0; i < leftArr.length; i ++) {
  //   ans += Math.min(leftArr[i], rightArr[i])
  // }
  // return ans


  // sol2 124ms 29%
  // O(n) O(1)
  // two pointer
  //
  let left = 0; let right = height.length-1
  let leftMax = height[0]; let rightMax = height[height.length-1]
  let ans = 0
  while (left < right) {
    if (height[left] < height[right]) {
      if (leftMax < height[left]) {
        leftMax = height[left]
      } else {
        ans += leftMax-height[left]
      }
      left += 1
    }
    else {
      if (rightMax < height[right]) {
        rightMax = height[right]
      } else {
        ans += rightMax-height[right]
      }
      right -= 1
    }
  }
  return ans
};

console.log(trap([0,1,0,2,1,0,1,3,2,1,2,1]))
console.log(trap([4,2,0,3,2,5]))

