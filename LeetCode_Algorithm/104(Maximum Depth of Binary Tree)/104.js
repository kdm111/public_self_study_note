var solve = function(node) {
  if (!node) {
    return 0;
  }
  return Math.max(solve(node.left), solve(node.right))+1
}
var maxDepth = function(root) {
  // O(n) O(n) 93ms 67%
  // return solve(root)    

  // 106ms 46%
  // let queue = [[0,root]]; let ans = 0
  // while (queue.length > 0) {
  //   temp = queue.shift()
  //   ans = Math.max(ans, temp[0])
  //   if (temp[1] != undefined) {
  //     queue.push([temp[0]+1, temp[1].left]);
  //     queue.push([temp[0]+1, temp[1].right]); 
  //   }
  // }
  // return ans

  // sol4 65ms 76% 44.8MB 84%
  if (!root) {
    return 0
  }
  return Math.max(maxDepth(root.left), maxDepth(root.right)) + 1
};