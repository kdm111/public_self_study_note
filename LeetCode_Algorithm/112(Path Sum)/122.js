var hasPathSum = function(root, targetSum) {
  // sol1 75ms 92%
  // O(n) O(n)
  return (dfs(root, targetSum))
};
var dfs = function(node, targetSum) {
  if (node) {
    targetSum -= node.val
    if (!node.left && !node.right && targetSum == 0) {
      return true
    }
    return dfs(node.left, targetSum) || dfs(node.right, targetSum)
  }
  return false
}
