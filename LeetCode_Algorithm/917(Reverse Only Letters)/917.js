var isalpha = (c) => {
  if (c >= 'a' && c <= 'z') 
    return true
  if (c >= 'A' && c <= 'Z')
    return true
  return false
}
var reverseOnlyLetters = function(s) {
  // sol2 68ms 61% 42.3MB 47%
  // let eng = []; let others = []
  // let ans = []
  // for (let c of s) {
  //   if (isalpha(c))
  //     eng.push(c)
  //   else
  //     others.push(c)
  // }
  // for (let i =0; i <s.length; i++) {
  //   if (isalpha(s[i])) {
  //     let c = eng.pop()
  //     ans.push(c)
  //   } else {
  //     let c = others.shift()
  //     ans.push(c)
  //   }
  // }
  // return ans.join("")

  // sol3 51ms 63% 42.29MB 44MB
  let ans = ""
  let i = 0; let j = s.length-1
  while (i < s.length) {
    if (!isalpha(s[i])) {
      ans += s[i]
    } else {
      while (j > 0 && !isalpha(s[j])) {
        j -= 1
      }
      ans += s[j]
      j -= 1
    }
    i += 1
  }
  return ans
};

console.log(reverseOnlyLetters("ab-cd"))