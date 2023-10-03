var calculate = function(s) {
  // sol1 168ms 16%
  let stack = []; let temp = -1
  // 10 이상의 자리
  for (let char of s) {
    if (char == ' ') {continue}
    if ('/' < char && char < ':') {
      if (temp < 0) {temp = 0}
      temp = (10*temp)+parseInt(char)
    } else {
      if (temp >=0){ stack.push(temp); temp = -1}
      stack.push(char)
    }
  }
  if (temp >= 0) {
    stack.push(temp); temp = -1
  }

  // 곱셈과 나눗셈
  let stack2 = []
  for (let t of stack) {
    if (stack2 && stack2[stack2.length-1] == '*') {
      stack2.pop()
      stack2.push(stack2.pop() * t)
    } else if (stack2 && stack2[stack2.length-1] == '/') {
      stack2.pop()
      stack2.push(parseInt(stack2.pop() / t))
    } else {
      stack2.push(t)
    }
  }

  // 덧셈과 뺄셈
  let ans = []
  for (let t of stack2) {
    if (ans && ans[ans.length-1] == '+') {
      ans.pop()
      ans.push(ans.pop() + t)
    } else if (ans && ans[ans.length-1] == '-') {
      ans.pop()
      ans.push(ans.pop() - t)
    } else {
      ans.push(t)
    }
  }
  return ans[0]
};

console.log(calculate("10*2-3/4+5*6-7*8+9/10"))