var sumOfLeftLeaves = function(root) {
  // sol1 65ms 96% 44.5% 48%
  // O(n) O(n)
  stack = [root]; ans = 0
  while (stack.length) {
    let node = stack.pop()
    if (node != undefined) {
      if (node.left != undefined) {
        stack.push(node.left)
        if (node.left.left == null && node.left.right == null) {
          ans += node.left.val
        }
      }
      if (node.right != undefined) {
        stack.push(node.right)
      }
    }
  }
  return ans
  
};