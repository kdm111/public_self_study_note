
function TreeNode(val, left, right) {
  this.val = (val===undefined ? 0 : val)
  this.left = (left===undefined ? null : left)
  this.right = (right===undefined ? null : right)
}

function makeTree(root, idx) {
  let rootNode = new TreeNode(root[idx])
  if (2*idx+1 < root.length) {rootNode.left = makeTree(root,2*idx+1)}
  if (2*idx+2 < root.length) {rootNode.right = makeTree(root,2*idx+2)}
  return rootNode 
}
function solve(root) {
  if (root == undefined) {return [true, -1]}
  let leftResult = solve(root.left); let rightResult = solve(root.right);
  if (leftResult[0] == false || rightResult[0] == false) {return [false, 0]}
  let r1 = Math.abs(leftResult[1]-rightResult[1]) < 2
  let r2 = 1+Math.max(leftResult[1], rightResult[1])
  return [r1, r2]
}
var isBalanced = function(root) {
  // 127ms 30%
  let rootNode = makeTree(root, 0)
  return solve(rootNode)[0]
};

console.log(isBalanced([3,9,20,null,null,15,7]))