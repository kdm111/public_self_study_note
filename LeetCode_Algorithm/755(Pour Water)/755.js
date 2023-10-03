var pourWater = function(heights, volume, k) {
  // sol1 72ms 84% 42.2MB 46%
  let l = heights.length; let idx = k
  while (volume > 0) {
    while (idx > 0 && heights[idx] >= heights[idx-1])
      idx -= 1
    while (idx < l && heights[idx] >= heights[idx+1])
      idx += 1
    while (idx > k && heights[idx] == heights[idx-1])
      idx -= 1
    heights[idx] += 1
    volume -= 1
  }  
  return heights
};