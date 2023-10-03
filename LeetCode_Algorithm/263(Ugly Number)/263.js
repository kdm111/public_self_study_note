var isUgly = function(n) {
  // sol 169ms 97%
  if (n < 1) {
    return false
  }
   for (let i of [2,3,5]) {
      while (n % i == 0) {
        n /= i
      }
   }
   if (i == 1) {
    return true
   } else {
    return false
   }
  
};
