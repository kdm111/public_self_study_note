function solve(root) {
  if (!root) {
    return 0
  }
  let leftGain = Math.max(solve(root.left), 0)
  let rightGain = Math.max(solve(root.right), 0)
  let temp = leftGain+root.val+rightGain
  if (ans < temp) {
    ans = temp
  }
  return root.val+Math.max(leftGain, rightGain)
  
}
var maxPathSum = function(root) {
  // O(n) O(h): height 90ms 88%
  ans = -Infinity
  solve(root)
  return ans
};

// console.log(maxPathSum(root))