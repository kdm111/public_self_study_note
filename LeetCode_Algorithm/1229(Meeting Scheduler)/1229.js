var quickSort= function (arr) {
  if (arr.length < 2) {
    return arr
  }
  let less = []; let equal = []; let greater = []
  let pivot = arr[parseInt(arr.length/2)][0]
  for (let [num, temp] of arr) {
    if (num < pivot) {
      less.push([num, temp])
    } else if (num == pivot) {
      equal.push([num, temp])
    } else {
      greater.push([num, temp])
    }
  }
  return quickSort(less).concat(equal.concat(quickSort(greater)))
}
var minAvailableDuration = function(slots1, slots2, duration) {
  // sol1 362ms 6%
  // two pointer
  slots1 = quickSort(slots1)
  slots2 = quickSort(slots2)

  let idx1 = 0; let idx2 = 0
  console.log(slots1, slots2)
  while (idx1 < slots1.length && idx2 < slots2.length) {
    let start = Math.max(slots1[idx1][0], slots2[idx2][0])
    let end = Math.min(slots1[idx1][1], slots2[idx2][1])
    if (end-start > duration || end-start==duration) {
      return [start, start+duration]
    }
    if (slots1[idx1][1] < slots2[idx2][1]) {
      idx1 += 1
    } else{
      idx2 += 1
    }
  }
  return []
};

console.log(minAvailableDuration([[10,50],[60,120],[140,210]], [[0,15],[60,70]], 8))