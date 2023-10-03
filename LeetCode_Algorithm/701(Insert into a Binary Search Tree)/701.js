function TreeNode(val, left, right) {
  this.val = (val===undefined ? 0 : val)
  this.left = (left===undefined ? null : left)
  this.right = (right===undefined ? null : right)
}

var insertIntoBST = function(root, val) {
  // sol1 133ms 19% 53.8MB 5%
  if (!root)
    return new TreeNode(val)
  if (root.val < val)
    root.right = insertIntoBST(root.right, val)
  else
    root.left = insertIntoBST(root.left, val)
  return root
};