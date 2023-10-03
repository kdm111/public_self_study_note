var getLonelyNodes = function(root) {
  // O(n) O(1) 89ms 86%
  let queue = [root]; let ans = []
  while (queue.length) {
    node = queue.shift()
    if (node.left && !node.right){
      ans.push(node.left.val)
    }
    if (node.right && !node.left) {
      ans.push(node.right.val)
    }
    if (node.left) {
      queue.push(node.left)
    }
    if (node.right) {
      queue.push(node.right)
    }
  }
  return ans
};