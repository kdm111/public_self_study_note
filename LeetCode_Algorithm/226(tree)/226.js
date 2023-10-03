function TreeNode(val, left, right) {
    this.val = (val===undefined ? 0 : val)
    this.left = (left===undefined ? null : left)
    this.right = (right===undefined ? null : right)
}
var invertTree = function(root) {
  // sol1 O(n), O(h) 69~105ms 70~14%
  // h는 tree의 높이
  if (root == null) {return null}
  var rootNode = makeTree(root, 0)
  invert(rootNode)
  return rootNode
  
};
var makeTree = function(root, idx){
  var rootNode = new TreeNode(root[idx])
  if (2*idx+1 < root.length) {rootNode.left = makeTree(root, 2*idx+1)}
  if (2*idx+2 < root.length) {rootNode.right = makeTree(root, 2*idx+2)}
  return rootNode
}
var invert = function(rootNode) {
  var temp = rootNode.left
  rootNode.left = rootNode.right
  rootNode.right = temp
  if (rootNode.left != undefined) {invert(rootNode.left)}
  if (rootNode.right != undefined) {invert(rootNode.right)}
}