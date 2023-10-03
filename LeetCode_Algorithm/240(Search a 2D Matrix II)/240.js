var searchMatrix = function(matrix, target) {
  // sol1 424ms 90% 44.7MB 75%
  let r = matrix.length-1; let c = 0
  while (r >= 0 && c < matrix[0].length) {
      if (matrix[r][c] == target)
        return true
      if (matrix[r][c] > target)
        r -= 1
      else
        c += 1
  }  
  return false
};