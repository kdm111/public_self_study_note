function TreeNode(val, left, right) {
    this.val = (val===undefined ? 0 : val)
    this.left = (left===undefined ? null : left)
    this.right = (right===undefined ? null : right)
}

var deleteNode = function(root, key) {
  // sol1 85ms 94% 50.6MB 89%
  if (!root) {return null}
  if (root.val > key) {
    root.left = deleteNode(root.left, key)
  }
  else if (root.val < key) {
    root.right = deleteNode(root.right, key)
  }
  else {
    if (!root.left && !root.right)
      root = null
    else if (root.right) {
      root.val = findVal(root.right)
      root.right = deleteNode(root.right, root.val)
    }
    else {
      root.val = findVal2(root.left)
      root.left = deleteNode(root.left, root.val)
    }
  }  
  return root
};
var findVal = function(node) {
  while (node.left) {
    node = node.left
  }
  return node.val
}
var findVal2 = function(node) {
  while (node.right) {
    node = node.right
  }
  return node.val
}