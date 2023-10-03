
var solve = (node, currMax, currMin) => {
  if (!node)
    return Math.abs(currMax - currMin)
  currMax = Math.max(currMax, node.val)
  currMin = Math.min(currMin, node.val)
  let left = solve(node.left, currMax, currMin)
  let right = solve(node.right, currMax, currMin)
  return Math.max(left, right)
}
var maxAncestorDiff = function(root) {
  // sol1 73ms 63% 45 MB 70%
  if (!root)
    return 0;
  return solve(root, root.val, root.val)
};