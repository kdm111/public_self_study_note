var checkPerfectNumber = function(num) {
  // sol1 91ms 91% 41.6MB 86%
  if (num <= 0) {
    return false
  }  
  let total = 0
  for (let i = 1; i * i <num; i++) {
    if (num % i == 0) {
      total += i
      if (i * i != num) {
        total += num / i
      }
    }
  }
  return total == 2 * num
};