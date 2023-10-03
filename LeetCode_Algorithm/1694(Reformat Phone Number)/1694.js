var reformatNumber = function(number) {
  // sol1 58ms 98% 42.3MB 60%
  number = number.replaceAll("-", "").replaceAll(" ", "")
  let i = 0; let ans = []
  while (i < number.length) {
    if (i+4 == number.length) {
      ans.push(number.slice(i, i+2))
      i += 2
    } else if (i+3 <= number.length) {
      ans.push(number.slice(i, i+3))
      i += 3
    } else{
      ans.push(number.slice(i, i+2))
      i += 2
    }
  }
  return ans.join("-")
};