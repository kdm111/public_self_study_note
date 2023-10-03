var reverseWords = function(s) {
  // sol1 219ms 5%
  // let ans = ""; let temp = ""
  // for (let c of s) {
  //   if (c == ' ') {
  //     ans += temp.split("").reverse().join("")
  //     ans += ' '
  //     temp = ""
  //   } else {
  //     temp += c
  //   }
  // }
  // ans += temp.split("").reverse().join("")
  // return ans


  // sol2 80ms 8% 52.45MB 5%
  s = Array(...s)
  let left = 0; let right = 0
  while (right < s.length) {
    while (right < s.length && s[right] != ' '){
      right +=1
    }
    right -= 1
    while (left < right) {
      let temp = s[left]
      s[left] = s[right]
      s[right] = temp
      left += 1; right -= 1
    }
    while (left < s.length && s[left] != ' '){
      left += 1
    }
    left += 1
    right = left
  }
  return s.join("")
};

console.log(reverseWords("abc def"))
console.log(reverseWords("Let's take LeetCode contest"))
