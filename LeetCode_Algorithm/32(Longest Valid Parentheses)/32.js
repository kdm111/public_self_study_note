var longestValidParentheses = function(s) {
  // sol1 78ms 65% 44.4MB 44%
  let stack = [-1]; let ans = 0
  for (let i =0; i < s.length; i++) {
    if (s[i] == '(')
      stack.push(i)
    else {
      stack.pop()
      if (stack.length == 0)
        stack.push(i)
      ans = Math.max(ans, i - stack[stack.length-1])
    }
    return ans
  }  
};