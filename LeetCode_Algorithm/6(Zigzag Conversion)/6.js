var convert = function(s, numRows) {
  // sol1 64ms 96% 45MB 84%
  if (s.length <= numRows || numRows == 1) {return s}
  let ans = new Array(numRows).fill("")
  let val = 2 * numRows - 2
  for (let i = 0; i < s.length; i++) {
    let pos = i % val  
    if (pos >= numRows) {
      ans[val - pos] += s[i]
    } else {
      ans[pos] += s[i]
    }
  }
  return ans.join("")
};
console.log(convert("PAYPALISHIRING", 3))