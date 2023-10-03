var solve = (node) => {
  if (!node)
    return ;
  for (let child of node.children)
    solve(child)
  ans.push(node.val)
}
var postorder = function(root) {
  // sol1 79ms 76% 46MB 19%
  ans = []
  solve(root)
  return ans  
};