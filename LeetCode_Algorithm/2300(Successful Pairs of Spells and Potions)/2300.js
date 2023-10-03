var successfulPairs = function(spells, potions, success) {
  // sol2 327ms 60% 76.2MB 46%
  potions.sort((a,b) => {return a-b})
  let numberOfPotions = potions.length
  let ans = Array(spells.length)
  for (let i = 0; i < spells.length ; i++) {
    ans[i] = numberOfPotions - binarySearchFindMinIdx(potions, success / spells[i])
  }
  return ans

};
var binarySearchFindMinIdx = (arr, target) => {
  let l = 0; let r = arr.length
  while (l < r) {
    let m = Math.floor((l + r) / 2)
    if (arr[m] >= target) {
      r = m
    } else {
      l = m + 1
    }
    
  }
  return l
}

console.log(successfulPairs([5,1,3], [1,2,3,4,5], 7))