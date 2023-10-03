var removeStars = function(s) {
  // sol 105ms 68%
  let stack = []
  for (let c of s) {
    if (c == '*') {
      if (stack.length) {
        stack.pop()
      }
    } else {
      stack.push(c)
    }
  }  
  return stack.join("")
};