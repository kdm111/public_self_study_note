memo = new Map()
var diffWaysToCompute = function(input) {
  // sol1 71ms 94%
  // 어떤 수가 NaN 인지 체크할 경우 
  // == NaN 이 아닌 isNaN 함수 사용
  if (!isNaN(input)) {
    return [Number(input)]
  }
  if (memo[input]) {
    return memo[input]
  }
  let ans = [];
  for (let i = 0; i < input.length; i++) {
    if (input[i] == '+' || input[i] == '-' || input[i] == '*') {
      let left = diffWaysToCompute(input.slice(0, i));
      let right = diffWaysToCompute(input.slice(i+1));
      for (let l of left) {
        for (let r of right) {
          ans.push(cal(l,input[i],r))
          }
        }
      }
  }
  memo[input] = ans
  return ans
};
var cal = function(m,op,n) {
  if (op == '+'){
    return m+n
  } else if (op == '-') {
    return m-n
  } else {
    return m*n
  }
}
// console.log(diffWaysToCompute("2-1-1"))
console.log(diffWaysToCompute("2*3-4*5"))
