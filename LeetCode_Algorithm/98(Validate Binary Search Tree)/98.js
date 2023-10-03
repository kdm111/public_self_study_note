function TreeNode(val, left, right) {
  this.val = (val===undefined ? 0 : val)
  this.left = (left===undefined ? null : left)
  this.right = (right===undefined ? null : right)
}
function makeTree(root, idx) {
  rootNode = new TreeNode(root[idx])
  if (2*idx+1 < root.length && root[2*idx+1] != undefined) {
    makeTree(root, 2*idx+1)
  }
  if (2*idx+2 < root.length && root[2*idx+2] != undefined) {
    makeTree(root, 2*idx+2)
  }
  return rootNode
}
var isValidBST = function(root) {
  rootNode = makeTree(root, 0)  
  stack = [[rootNode, -Infinity, Infinity]]
  // preorder O(n) 146ms 8%
  while (stack.length > 0) {
    temp = stack.pop()
    node = temp[0]; lower = temp[1]; upper = temp[2]
    if (node.val <= lower || upper <= node.val) {
      return false
    }
    if (node.right != undefined) {
      stack.push([node.right, node.val, upper])
    }
    if (node.left != undefined) {
      stack.push([node.left, lower, node.val])
    }
  }
  return true
};


console.log(isValidBST([2,1,3]))