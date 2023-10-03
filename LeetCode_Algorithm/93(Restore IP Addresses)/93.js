var restoreIpAddresses = function(s) {
  // sol1 66ms 89% 42.4MB 85%
  ans = []
  solve(s, [])
  return ans
};
var solve = (s, temp) => {
  if (temp.length == 4) {
    let string = temp.join("")
    string = string.slice(0, string.length-1)
    ans.push(string)
    return ;
  }
  let i = 1;
  while (i < 4 && i <= s.length) {
    let num = s.slice(0, i)
    if (num.length > 1 && num[0] == '0') {
    i += 1; continue
    }
    if (0 <= parseInt(num) && parseInt(num) <= 255) {
    num += '.'
    temp.push(num)
    solve(s.slice(i, ), temp)
    temp.pop()
    }
    i += 1
    }
}