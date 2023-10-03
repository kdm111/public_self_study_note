function TreeNode(val) {
  this.val = val
  this.left = this.right = null

}
function makeTree(root, idx) {
  var rootNode = new TreeNode(root[idx])
  if (2*idx+1 < root.length) {
    rootNode.left = makeTree(root, 2*idx+1)
  }
  if (2*idx+2 < root.length) {
    rootNode.right = makeTree(root, 2*idx+2)
  }
  return rootNode
}

var lowestCommonAncestor = function(root, p, q) {
  rootNode = makeTree(root, 0)
  // O(n) 101ms 76%
  while (rootNode != null) {
    if (p < rootNode.val && q < rootNode.val) {
      rootNode = rootNode.left
    }
    else if (rootNode.val < p && rootNode.val < q) {
      rootNode = rootNode.right
    }
    else {
      return rootNode.val
    }
  }

};

console.log(lowestCommonAncestor([6,2,8,0,4,7,9,null,null,3,5], 2, 4))