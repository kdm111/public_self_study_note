var increasingTriplet = function(nums) {
  // sol1 81ms 78% 61.4MB 18%
  let first = Infinity
  let second = Infinity  
  for (let num of nums) {
    if (num <= first) {
      first = num
    } else if (num <= second) {
      second = num
    } else {
      return true
    }
  }
  return false
};

