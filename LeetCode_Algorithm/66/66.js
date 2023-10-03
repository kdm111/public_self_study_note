var plusOne = function(digits) {
// sol1 O(n), O(n) 61~67ms 86~74% 
  for (let i=digits.length-1; i > -1 ; i--) {
    digits[i] += 1
    if (digits[i] == 10) {
      digits[i] = 0
      if (i == 0) { 
        digits.unshift(1)
        return digits
      }
    }
    else  {
      break
    }
  }
  return digits
};

console.log(plusOne([9,9,9]))