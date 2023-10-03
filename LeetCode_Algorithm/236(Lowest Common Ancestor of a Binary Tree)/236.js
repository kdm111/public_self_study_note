var solve = (root, p, q) => {
  if (!root)
    return null;
  let left = solve(root.left, p, q)
  let right = solve(root.right, p, q)
  let mid = (root.val == p.val) || (root.val == q.val)
  if (mid + left + right >= 2)
    ans = root
  return mid || left || right
}
var solve2 = (node, p, q) => {
  if (!node)
    return false
  if (node.val == p.val || node.val == q.val)
    return node
  let left = solve2(node.left, p, q)
  let right = solve2(node.right, p, q)
  if (left && right)
    return node
  if (left)
    return left
  return right
}
var lowestCommonAncestor = function(root, p, q) {
  // sol1 91ms 63% 52MB 31%
  ans = null
  solve(root, p, q)
  return ans
  // sol2 64ms 91% 51.3MB 75%
  return solve2(root, p, q)
};