
function TreeNode(val, left, right) {
  this.val = (val===undefined ? 0 : val)
  this.left = (left===undefined ? null : left)
  this.right = (right===undefined ? null : right)
}

var longestZigZag = function(root) {
  // sol1 139ms 92% 93.24MB 9%
  function solve(node, dir, cnt) {
    if (!node)
      return cnt
    if (dir === 'l') {
      return Math.max(solve(node.left, 'l', 0), solve(node.right, 'r', cnt+1))
    } else {
      return Math.max(solve(node.left, 'l', cnt+1), solve(node.right, 'r', 0))
    }
  }    
  return Math.max(solve(root.left, 'l', 0), solve(root.right, 'r', 0))
};