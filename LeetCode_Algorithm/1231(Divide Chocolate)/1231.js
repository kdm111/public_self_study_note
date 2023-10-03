var check = function(sweetness, mid, num) {
  let currSum = 0; let cnt = 0
  for (let choco of sweetness) {
    currSum += choco
    if (currSum > mid || currSum == mid) {
      cnt += 1; currSum = 0
    }
  }
  if (cnt == num || cnt > num) {
    return true
  }
  return false
}

var maximizeSweetness = function(sweetness, k) {
  // 150ms 6%
  let left = Math.min(...sweetness)
  let right = sweetness.reduce((a,b) =>a+b, 0)
  right = parseInt(right/(k+1))
  while (left < right) {
    let mid = parseInt((left+right+1) / 2)
    console.log(left, mid, right)
    if (check(sweetness, mid, k+1)) {
      left = mid
    } else {
      right = mid-1
    }
  }
  return left
};

console.log(maximizeSweetness([1,2,3,4,5,6,7,8,9], 5))