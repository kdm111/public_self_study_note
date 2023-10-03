function TreeNode(val, left, right) {
  this.val = (val===undefined ? 0 : val)
  this.left = (left===undefined ? null : left)
  this.right = (right===undefined ? null : right)
}
function makeTree(lst, idx) {
  if (idx > lst.length-1) {
    return null
  }
  let root = new TreeNode(lst[idx])
  root.left = makeTree(lst, 2*idx+1)
  root.right = makeTree(lst, 2*idx+2)
  return root
}

var isSameTree = function(p, q) {
  let pNode = makeTree(p,0)
  let qNode = makeTree(q,0)
  // O(n) O(1) 87ms 48%
  lst = []; lst.push([pNode,qNode])
  while (lst.length > 0) {
    temp = lst.shift()
    pNode = temp[0]; qNode = temp[1]
    // console.log(pNode, qNode)
    if (pNode == null && qNode == null) {
      continue
    }
    if (!(pNode) || !(qNode)) {
      // console.log(pNode, qNode)
      return false
    }
    if (pNode.val != qNode.val) {
      // console.log(pNode, qNode)
      return false
    }
    lst.push([pNode.left, qNode.left])
    lst.push([pNode.right, qNode.right])
  } 
  return true
};

console.log(isSameTree([1,2,3], [1,2,3]))


