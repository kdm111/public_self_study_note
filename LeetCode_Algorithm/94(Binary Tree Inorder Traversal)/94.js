var dfs = function(node) {
  if (node) {
    dfs(node.left)
    ans.push(node.val)
    dfs(node.right)
  }
}
var inorderTraversal = function(curr) {
  // sol1 91ms 53%
  // O(n) O(n)
  // ans = []  
  // dfs(curr)
  // return ans


  // sol2 77ms 74%
  // iter 
  // ans = []; stack = []; node = curr
  // while (node || stack.length) {
  //   while (node) {
  //     stack.push(node)
  //     node = node.left
  //   }
  //   node = stack.pop()
  //   ans.push(node.val)
  //   node = node.right
  // }
  // return ans


  // sol3 84ms 65%
  // Morris Traversal
  ans = []; curr = root
  while (curr) {
    if (curr.left == null) {
      ans.push(curr.val)
      curr = curr.right
    } else {
      prev = curr.left
      while (prev.right) {
        prev = prev.right
      }      
      prev.right = curr
      temp = curr
      curr = curr.left
      temp.left = null
    }
  }
  return ans

};