var solve = (node, nodeVal) => {
  if (!node)
    return ;
  if (node.val >= nodeVal) {
    ans += 1
    nodeVal = node.val
  }
  solve(node.left, nodeVal)
  solve(node.right, nodeVal)
}
var goodNodes = function(root) {
  // sol1 147ms 85% 64.9MB 78%
  if (!root)
    return 0
  ans = 0
  solve(root, root.val)
  return ans
};