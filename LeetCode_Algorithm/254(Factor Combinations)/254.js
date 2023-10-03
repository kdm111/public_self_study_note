var solve = function(n, arr) {
  console.log(n)
  if (arr.length > 0) {
    let temp = arr.slice()
    temp.push(n)
    ans.push(temp)
  }
  for (let k=2; k < parseInt(Math.sqrt(n))+1; k++) {
    if (n % k == 0) {
      if (arr.length && k < arr[arr.length-1]){
        continue
      }
      let temp = arr.slice()
      temp.push(k)
      solve(parseInt(n/k), temp)
    }
  }
}
var getFactors = function(n) {
  // sol2 205ms 71%
  ans = []
  solve(n, [])
  return ans
  
};

console.log(getFactors(8))
console.log(getFactors(12))
