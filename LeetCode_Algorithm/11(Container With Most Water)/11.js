var maxArea = function(height) {
  // sol2 80ms 58% 49.9MB 21%
  let left = 0; let right = height.length-1
  let ans = 0
  while (left < right) {
    let temp = (right-left) * Math.min(height[left], height[right])
    ans = Math.max(temp, ans)
    if (height[left] < height[right]) {
      left += 1
    } else {
      right -= 1
    }
  }  
  return ans
};