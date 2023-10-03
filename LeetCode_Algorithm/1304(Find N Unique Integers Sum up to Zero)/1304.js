var sumZero = function(n) {
  // sol1 94ms 69% 42.3MB 78%
  if (n % 2) {
    ans = [0]
  } else {
    ans = []
  }
  for (let i = 1; i < parseInt(n / 2)+1; i++) {
    ans.push(i, -i)
  }
  return ans
};