 function TreeNode(val, left, right) {
  this.val = (val===undefined ? 0 : val)
  this.left = (left===undefined ? null : left)
  this.right = (right===undefined ? null : right)
}
var buildTree = function(inorder, postorder) {
  // sol3 67ms 93% 44.6MB 92%
  let mapInorder = {}
  for (let [i, val] of inorder.entries()) {
    mapInorder[val] = i
  }
  function solve(l, r) {
    if (l > r) {return null}
    const node = new TreeNode(postorder.pop())
    const m = mapInorder[node.val]
    node.right = solve(m+1, r)
    node.left = solve(l, m-1)
    return node    
  }
  return solve(0, inorder.length-1)
};

console.log(buildTree([9,3,15,20,7], [9,15,7,20,3]))