var reverseWords = function(s) {
  // sol1 103ms 56% 45.1MB 14%
  let start = 0
  while (s[start] == ' ')
    start += 1
  let left = right = s.length-1
  while (s[left] == ' ')
    left -= 1
  ans = ""
  while (left >= start) {
    right = left
    while (left >= start && s[left] != ' ')
      left -= 1
    ans += s.slice(left+1, right+1)
    while (left >= start && s[left] == ' ')
      left -= 1
    if (left >= start) {
      ans += ' '
    }
  }
  return ans
  
  // sol2 111ms 40% 43.7MB 90%
  // 정규 표현식으로 해보려던 방법
  // return s.split(/^\s+|\s+$|\s+/).reverse().join(' ')
  return s.trim().split(/\s+/).reverse().join(' ')
  
};

console.log(reverseWords("   The    sky blue  "))