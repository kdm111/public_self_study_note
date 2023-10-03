var deleteAndEarn = function(nums) {
  // sol1 60ms 96% 45% 76%
  let cnt = new Array(Math.max(...nums)+1).fill(0)  
  for (let num of nums) {
    cnt[num] += num
  }
  let prev = 0; let curr = 0; let temp = 0
  for (const v of cnt) {
    temp = curr; 
    curr = Math.max(prev + v, curr)
    prev = temp
  }
  return curr
};

console.log(deleteAndEarn([2,4,3]))