var transformArray = function(arr) {
  // sol1 100ms 57% 41.7MB 71%
  if (arr.length < 3)
    return arr
  let changed = true
  while (changed) {
    changed = false
    let prev = arr[0]; let curr = arr[1]; let next = arr[2]
    for (let i = 1; i < arr.length-1; i++) {
      if (curr > prev && curr > next) {
        arr[i] -= 1; changed = true
      } else if (curr < prev && curr < next) {
        arr[i] += 1; changed = true
      }
      if (i < arr.length-2) {
        prev = curr; curr = next; next = arr[i+2]
      } else {
        break
      }
    }
  }  
  return arr
};
console.log(transformArray([1,6,3,4,3,5]))