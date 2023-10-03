var calculate = function(s) {
  // 136ms 12% 52.7MB 12%
  let stack = [];
  for (let c of s) {
    if (c == ' ') {
      continue
    } else if (c == ')') {
      let temp = []
      while (stack.length && stack[stack.length-1] != '(') {
        temp.push(stack.pop())
      }
      stack.pop()
      temp.reverse()
      stack.push(cal(temp))
    } else if (c == '+' || c == '-' || c == '(') {
      stack.push(c)
    } else {
      if (Number.isInteger(stack[stack.length-1])) {
        m = stack.pop()
        stack.push(10 * m + Number(c))
      } else {
        stack.push(Number(c))
      }
    }
  }  
  return cal(stack)
};

cal = (temp) => {
  if (temp[0] == '-') {
    ret = -temp[1]; temp.shift(); temp.shift()
  } else {
    ret = temp.shift()
  }
  while (temp.length) {
    m = temp.shift()
    if (m == '+') {
      ret += temp.shift()
    } else {
      ret -= temp.shift()
    }
  }
  return ret
}

console.log(calculate("2147483647"))