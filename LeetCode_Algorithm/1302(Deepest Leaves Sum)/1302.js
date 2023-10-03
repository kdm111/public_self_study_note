var deepestLeavesSum = function(root) {
  // sol1 189ms 51% 64.5MB 72%
  let queue = [root]
  while (queue.length) {
    let temp = []; let ans = 0
    for (let node of queue) {
      ans += node.val
      if (node.left)
        temp.push(node.left)
      if (node.right)
        temp.push(node.right)
    }
    queue = temp
  }
  return ans
};