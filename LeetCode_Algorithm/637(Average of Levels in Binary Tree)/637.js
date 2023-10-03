var averageOfLevels = function(root) {
  // sol1 143ms 22%
  let queue = [root]; let ans = []
  while (queue.length > 0) {
    let nodeSum = 0; let temp = []
    for (let node of queue) {
      nodeSum += node.val
      if (node.left) {
        temp.push(node.left)
      }
      if (node.right) {
        temp.push(node.right)
      }
    }
    ans.push(nodeSum / queue.length)
    queue = temp
  }
  return ans
};