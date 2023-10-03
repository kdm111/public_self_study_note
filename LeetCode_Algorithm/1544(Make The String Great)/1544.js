var toAscii = function(c) {
  return c.charCodeAt(0)
}
var makeGood = function(s) {
  // sol1 110ms 63% 44MB 67%

  let stack = []
  for (let c of s) {
    if (stack.length == 0) {
      stack.push(c)
    } else {
      if ('a' <= c && c <= 'z' && stack[stack.length-1] == c.toUpperCase()) {
        stack.pop()
      } else if ('A' <= c && c <= 'Z' && stack[stack.length-1] == c.toLowerCase()) {
        stack.pop()
      } else {
        stack.push(c)
      }
    }
  }
  return stack.join('')
};
console.log(makeGood("leEt"))