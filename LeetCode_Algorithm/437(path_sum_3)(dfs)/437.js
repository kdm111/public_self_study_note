function TreeNode(val, left, right) {
  this.val = (val===undefined ? 0 : val)
  this.left = (left===undefined ? null : left)
  this.right = (right===undefined ? null : right)
}
function makeTree(root, idx) {
  var rootNode = new TreeNode(root[idx])
  if (2*idx+1 < root.length) {rootNode.left = makeTree(root, 2*idx+1)}
  if (2*idx+2 < root.length) {rootNode.right = makeTree(root, 2*idx+2)}
  return rootNode
}
function solve(root, targetSum) {
  if (root == undefined || root.val == undefined) {
    return ;
  }
  findPath(root, targetSum)
  solve(root.left, targetSum)
  solve(root.right, targetSum)
}
function findPath(root, targetSum) {
  if (root == undefined || root.val == undefined) {
    return ;
  }
  if (root.val == targetSum) {
    ans += 1
  }
  findPath(root.left, targetSum-root.val)
  findPath(root.right, targetSum-root.val)
}
var pathSum = function(root, targetSum) {
  var root = makeTree(root, 0)
  // sol1 O(n^2) O(1) 77ms 68% 52.6MB 12%
  ans = 0
  solve(root, targetSum)
  return ans
};

console.log(pathSum([10,5,-3,3,2,null,11,3,-2,null,1], 8))