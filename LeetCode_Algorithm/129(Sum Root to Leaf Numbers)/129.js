var sumNumbers = function(root) {
  // sol1 49ms 95% 42.6MB 32%
  return solve(root, 0)
};

var solve = (node, val) => {
  if (!node)
    return 0
  if (!node.left && !node.right) {
    return (10 * val) + node.val
  }
  return solve(node.left, 10 * val + node.val) + solve(node.right, 10 * val + node.val)
}