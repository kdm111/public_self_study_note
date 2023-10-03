var searchMatrix = function(matrix, target) {
  // 91ms 44%
  const m = matrix.length; const n = matrix[0].length
  let left = 0; let right = m*n-1
  while (left < right || left == right) {
    let mid = left + parseInt((right-left) / 2)
    let r = parseInt(mid / n); let c = mid % n
    if (target == matrix[r][c]) {
      return true
    } else if (target < matrix[r][c]) {
      right = mid -1
    } else {
      left = mid + 1
    }
  }
  return false
};
console.log(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))