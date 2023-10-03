var dfs = function(node) {
  if (node) {
    dfs(node.left)
    dfs(node.right)
    ans.push(node.val)
  }
}
var postorderTraversal = function(root) {
  // sol1 97ms 37%
  // ans = []
  // dfs(root)
  // return ans


  // sol2 124ms 5%
  let ans = []; 
  let curr = root
  let stack = [curr]
  while (stack.length) {
    curr = stack.pop()
    if (curr) {
      ans.push(curr.val)
      stack.push(curr.left)
      stack.push(curr.right)
    }
  } å
  ans.reverse()
  return ans
};