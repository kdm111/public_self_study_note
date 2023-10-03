function TreeNode(val, left, right){
  this.val = (val===undefined ? 0 : val)
  this.left = (left===undefined ? null : left)
  this.right = (right===undefined ? null : right)
}

var diameterOfBinaryTree = function(root) {
  // sol1 68~123ms 96~29%보다 빠름
  this.diameter = 0
  var rootNode = makeTree(root, 0)
  postOrderTraversal(rootNode)
  return this.diameter
};
function makeTree(root, idx){
  var rootNode = new TreeNode(root[idx])
  if (2*idx+1 < root.length){
    rootNode.left = makeTree(root, 2*idx+1)
  }
  if (2*idx+2 < root.length){
    rootNode.right = makeTree(root, 2*idx+2)
  }
  return rootNode
}

function postOrderTraversal(node){
  if (node == null) {return 0}
  var leftDepth = 0
  var rightDepth = 0
  console.log(node)
  if (node.left){ leftDepth = postOrderTraversal(node.left)}
  if (node.right){ rightDepth = postOrderTraversal(node.right)}
  process.stdin.write(node.val + " ")
  this.diameter = Math.max(this.diameter, leftDepth+rightDepth)
  return Math.max(leftDepth, rightDepth)+1
}
console.log(diameterOfBinaryTree([1,2]))