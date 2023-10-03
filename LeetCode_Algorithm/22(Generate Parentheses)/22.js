var generateParenthesis = function(n) {
  // sol1 66ms 42% 42MB 89%
  var solve = (left, right, temp) => {
    if (temp.length == 2 * n) {
      ans.push(temp); return
    }
    if (left < n)
      solve(left+1, right, temp + '(')
    if (right < left)
      solve(left, right + 1, temp + ')')
  }
  ans = []
  solve(0, 0, "")
  return ans
};

console.log(generateParenthesis(2))