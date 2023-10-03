var solve = (node) => {
  if (!node)
    return []
  let left = solve(node.left)
  let right = solve(node.right)
  left.push(node.val)
  left.push(...right)
  return left
}
var getMinimumDifference = function(root) {
  // sol2 75ms 84% 49.9MB 11.8%
  // let ans = Infinity    
  // let val = solve(root)
  // for (let i = val.length-1; i > 0; i--) {
  //   ans = Math.min(ans, val[i] - val[i-1])
  // }
  // return ans


  // sol3 77ms 79% 48.9MB 18%
  let val = []
  let curr = root; let stack = []
  while (stack.length || curr) {
    if (curr) {
      stack.push(curr)
      curr = curr.left
    } else {
      curr = stack.pop()
      val.push(curr.val)
      curr = curr.right
    }
  }
  let ans = Infinity
  for (let i = val.length-1; i > 0 ; i--) {
    ans = Math.min(ans, val[i]- val[i-1])
  }
  return ans
};
