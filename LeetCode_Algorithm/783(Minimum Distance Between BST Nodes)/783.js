var solve = (node) => {
  if (!node)
    return ;
  solve(node.left)
  if (prev >= 0)
    ans = Math.min(ans, Math.abs(prev - node.val))
  prev = node.val
  solve(node.right)
}
var minDiffInBST = function(root) {
  // sol1 57ms 92% 43.3MB 44%
  ans = Infinity; prev = -1
  solve(root)  
  return ans
};