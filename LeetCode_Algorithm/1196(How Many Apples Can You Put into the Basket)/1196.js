var maxNumberOfApples = function(weight) {
  // sol1 71ms 84% 43.7MB 90%
  weight.sort((a,b) => {return a-b})  
  let ans = 0; let total = 5000
  for (let unit of weight) {
    if (unit > total)
      break
    total -= unit
    ans += 1
  }
  return ans
};
console.log(maxNumberOfApples([1,5,6]))