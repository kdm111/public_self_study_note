var largestValues = function(root) {
  // sol1 83ms 51% 47.8MB 8%
  if (!root)
    return []
  let ans = []
  let queue = [root]
  while (queue.length) {
    let temp = []; let val = queue[0].val
    for (let i=0; i < queue.length; i++) {
      val = Math.max(val, queue[i].val)
      if (queue[i].left) {
        temp.push(queue[i].left)
      }      
      if (queue[i].right) {
        temp.push(queue[i].right)
      }
    }
    queue = temp;
    ans.push(val)
  }
  return ans
};