var evalRPN = function(tokens) {
  // 문자열 to 숫자에서 == NaN 비교문을 사용하는 것이 아닌
  // isNaN함수를 사용하여 문제 해결해야 함
  // 67ms 73% 45.6MB 41%
  let stack = []
  for (let token of tokens) {
    if (!isNaN(token)) {
      stack.push(parseInt(token))
    } else {
      let num2 = stack.pop()
      let num1 = stack.pop()
      stack.push(cal(num1, token, num2))
    }
  }  
  return stack[stack.length - 1]
};
var cal = function(num1, operator, num2) {
  if (operator == '+')
    return (num1 + num2)
  else if (operator == '-')
    return (num1 - num2)
  else if (operator == '*')
    return (num1 * num2)
  else
    return parseInt(num1 / num2)
}

// console.log(parseInt("12") !== NaN)
console.log(isNaN(parseInt("+")))
console.log(isNaN(parseInt("12")))


console.log(evalRPN(["2","1","+","3","*"]))