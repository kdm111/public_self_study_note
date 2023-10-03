var reduce = function(nums, fn, init) {
  // sol1 63ms 47% 44.1MB 18%
  // let val = init
  // for (let num of nums) {
  //   val = fn(val, num)
  // }
  // return val

  // sol2 60ms 65% 42.7MB 38%
  let val = init
  nums.forEach((num) => {
    val = fn(val, num)
  })
  return val
};