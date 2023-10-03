var closestValue = function(root, target) {
  // sol1 80ms 35% 45.9MB 17%
  let ans = -1; 
  let absVal = Infinity
  let queue = [root]
  while (queue.length) {
    let node = queue.shift()
    if (absVal > Math.abs(node.val - target)) {
      absVal = Math.abs(node.val - target)
      ans = node.val
    }
    if (node.left)
      queue.push(node.left)
    if (node.right)
      queue.push(node.right)
  }
  return ans
};