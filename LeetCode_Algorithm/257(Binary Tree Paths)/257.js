var solve = (node, temp) => {
  if (!node) {
    return ;
  }
  if (!node.left && !node.right) {
    temp += String(node.val)
    ans.push(temp)
    return ;
  }
  temp += (String(node.val) + "->")
  solve(node.left, temp)
  solve(node.right, temp)
}
var binaryTreePaths = function(root) {
  // sol1 77ms 36% 43.5MB 70%
  ans = []
  solve(root, "")
  return ans
};