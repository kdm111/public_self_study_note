var rotate = function(nums, k) {
  // sol2 217ms 5%
  // let temp = new Array(nums.length)
  // for (let i=0; i < nums.length; i++) {
  //   idx = (i+k) % nums.length
  //   temp[idx] = nums[i]
  // }
  // for (let i=0; i < nums.length; i++) {
  //   nums[i] = temp[i]
  // }
  // return nums

  // sol3 215ms 5%
  // let n = nums.length
  // k %= n
  // let temp = nums.slice(n-k, ).concat(nums.slice(0,n-k))
  // for (let i=0; i < nums.length; i++) {
  //   nums[i] = temp[i]
  // }

  // sol4 179ms 22%
  let n = nums.length
  let start = 0;
  let cnt = 0
  while (cnt < n) {
    let curr = start; let prev = nums[curr]
    while (true) {
      let nextIdx = (curr+k) % n
      let temp = nums[nextIdx]
      nums[nextIdx] = prev
      prev = temp
      cnt += 1
      curr = nextIdx
      if (start == curr) {
        break ;
      }
    }
    start += 1
  } 

};
var swap = function(a,b) {
  
}
console.log(rotate([1,2,3,4,5,6], 2))