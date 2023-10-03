var widthOfBinaryTree = function(root) {
  // 137ms 21%
  if (!root) {return 0}
  let queue = []
  let left = 0; let curDepth = 0; let ans = 0;
  queue.push([root, 0, 0])
  while (queue.length > 0) {
    let temp = queue.shift()
    let node = temp[0]; let depth = temp[1]; let pos = temp[2]
    if (!node) {continue}
    queue.push([node.left, depth+1, 2*parseInt(pos)])
    queue.push([node.right, depth+1, 2*parseInt(pos)+1])
    if (curDepth != depth) {
      curDepth = depth; left = pos
    }
    ans = Math.max(ans, pos-left+1)
  }
  return ans
};

console.log()