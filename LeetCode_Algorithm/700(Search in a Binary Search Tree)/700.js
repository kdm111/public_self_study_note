var searchBST = function(root, val) {
  // sol1 80ms 67% 49.5MB 31%
  var solve = function(node) {
    if (!node)
      return null
    if (node.val == val)
      return node
    else {
      if (node.val < val)
        return solve(node.right)
      else
        return solve(node.left)
    }
  }
  return solve(root)
};