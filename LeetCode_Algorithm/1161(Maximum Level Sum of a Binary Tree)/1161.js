var maxLevelSum = function(root) {
  // sol1 147ms 90% 76.42MB 30%
  let level = 1; let total = root.val
  let ans = level; let queue = [root]
  while (queue.length) {
    let temp = 0; let tempQueue = []
    for (let node of queue) {
      temp += node.val
      if (node.left) {tempQueue.push(node.left)}
      if (node.right) {tempQueue.push(node.right)}
    }
    if (total < temp) {
      total = temp; ans = level
    }
    queue = tempQueue.slice(0, )
    level += 1
  }  
  return ans
};