function TreeNode(val, left, right) {
  this.val = (val !== undefined ? val : 0)
  this.left = (left !== undefined ? left : null)
  this.right = (right !== undefined ? right : null)

}
function makeTree(lst, idx) {
  if (idx > lst.length || idx == lst.length) {
    return null
  }
  var rootNode = new TreeNode(lst[idx])
  rootNode.left = makeTree(lst, 2*idx+1)
  rootNode.right = makeTree(lst, 2*idx+2)
  return rootNode
}

var kthSmallest = function(root, k) {
  var root = makeTree(root, 0)
  // 79ms 91%
  var lst = []
  while (true) {
    while (root != undefined) {
      lst.push(root)
      root = root.left
    }
    k -= 1
    root = lst.pop()
    if (k == 0) {
      return root.val
    }
    root = root.right
  }  
};
console.log(kthSmallest([3,1,4,null,2],2))