var isToeplitzMatrix = function(matrix) {
  // sol2 O(mn), O(m+n) 72~84ms 88~67%
  hashMap = new Map()
  for (const [idx, row] of matrix.entries()) {
    for (const [col, val] of row.entries()) {
      if (!hashMap.has(idx-col)){
        hashMap.set(idx-col, val)
      }
      else if(hashMap.get(idx-col) != val){
        return false
      }
    }
  }
  return true
};
console.log(isToeplitzMatrix([[1,2],[2,2]]))
