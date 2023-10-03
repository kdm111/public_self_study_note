function isAlpha(a) {
  return (typeof(a) == "string" && a.length == 1 &&
  (a >= 'a' && 'z' <= a || 'A' <= a && a <= 'Z'))
}
function isDigit(a) {
  return ( a >= '0' && '9' >= a )
}
var decodeString = function(s) {
  // sol1 O(n) 119ms 5%
  // stack = []
  // for (let c of s) {
  //   if (c == ']') {
  //     let string = ""
  //     while (stack.length > 0 && !isDigit(stack[stack.length-1])) {
  //       let temp = stack.pop()
  //       if (temp != '['){
  //         string += temp
  //       }
  //     }
  //     console.log(string)
  //     let num = ""
  //     while (stack.length > 0 && isDigit(stack[stack.length-1])) {
  //       let temp = stack.pop()
  //       if (isDigit(temp)){
  //         num += temp
  //       }
  //     }
  //     if (num != ""){
  //       num = parseInt(num.split("").reverse().join(""))
  //     }
  //     else {
  //       num = 1
  //     }
  //     while (num > 0) {
  //       for (let ch of string.split("").reverse().join("")) {
  //         stack.push(ch)
  //       }
  //       num -= 1
  //     }
  //   }
  //   else {
  //     stack.push(c)
  //   }
  // }
  // return stack.join("")


  // sol2 58ms 59% 41.74MB 65%
  let stack = []
  for (let c of s) {
    if (c == ']') {
      let temp = ""
      while (stack[stack.length-1] != '[') {
        temp += stack.pop()
      }
      stack.pop()
      let num = ""
      while (stack.length && '0' <= stack[stack.length-1] && stack[stack.length-1] <= '9') {
        num += stack.pop()
      }
      num = num.split('').reverse().join('')
      for (let _ = 0; _ < Number(num); _++) {
        stack.push(temp)
      }
    } else {
      stack.push(c)
    }
  }
  let ans = ""
  for (let i = 0; i < stack.length; i++) {
    ans += stack[i].split('').reverse().join('')
  }
  return ans
};

// console.log(decodeString("3[2[c]]"))
// console.log(decodeString("3[a]2[bc]"))
console.log(decodeString("100[a]"))
