var solve = (node) => {
  if (!node)
    return null
  if (!node.left && !node.right)
    return node
  let left = solve(node.left)
  let right = solve(node.right)
  if (left) {
    left.right = node.right
    node.right = node.left
    node.left = null
  }
  return right ? right : left
}
var flatten = function(root) {
  // 73ms 87% 43.5MB 99%
  solve(root)  
};