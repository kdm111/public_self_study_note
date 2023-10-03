function TreeNode(val, left, right) {
  this.val = (val===undefined ? 0 : val)
  this.left = (left===undefined ? null : left)
  this.right = (right===undefined ? null : right)
}
var buildTree = function(preorder, inorder) {
  // 171ms 43%
  if (inorder.length > 0) {
    let idx = inorder.indexOf(preorder.shift())
    let root = new TreeNode(inorder[idx])
    root.left = buildTree(preorder, inorder.slice(0 ,idx))
    root.right = buildTree(preorder, inorder.slice(idx+1, ))
    return root
  } else {
      return null
  }
};