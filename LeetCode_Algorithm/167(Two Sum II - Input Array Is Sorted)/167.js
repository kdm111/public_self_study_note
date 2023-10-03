var twoSum = function(numbers, target) {
  // 118ms 18%
  // let left = 0; let right = numbers.length-1
  // while (left < right) {
  //   let totalSum = numbers[left]+numbers[right]
  //   if (totalSum == target) {
  //     return [left+1, right+1]
  //   } else if (totalSum < target) {
  //     left += 1
  //   } else {
  //     right -=1
  //   }
  // }


  // sol2 450ms 5%
  hashMap = new Map()
  for (let [i,n] of numbers.entries()) {
    console.log(target-n)
    if (String(target-n) in hashMap) {
      return [hashMap[target-n]+1, i+1]
    }
    hashMap[n] = i
  }
  console.log(hashMap)
};

console.log(twoSum([2,7,11,15], 9))