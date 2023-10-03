var solve2 = (node, depth) => {
  // sol2 261ms 43% 83MB 70%
  if (!node || depth >= ans) 
    return 
  if (!node.left && !node.right) {
    ans = Math.min(ans, depth)
    return ;
  }
  solve2(node.left, depth+1)
  solve2(node.right, depth+1)
}
var minDepth = function(root) {
  // sol1 402ms 18%
  // O(n) O(2^d)
  if (!root) {
    return 0
  }  
  let queue = [[root, 1]]
  while (queue.length) {
    [node, n]= queue.shift()
    if (!node) {
      continue
    } else if (!node.left && !node.right) {
      return n
    } else {
      queue.push([node.left, n+1])
      queue.push([node.right, n+1])
    }
  }
};