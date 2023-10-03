var leafSimilar = function(root1, root2) {
  // sol1 87ms 77% 44.7MB 21%
  let root1Leaf = []; let root2Leaf = []
  traversal(root1, root1Leaf)
  traversal(root2, root2Leaf)

  // 
  // return root1Leaf.toString() == root2Leaf.toString() // js는 객체를 문자열로 만들어 리턴하는 것이 더 빠르다.
  if (root1Leaf.length != root2Leaf.length) {
    return false
  }
  for (let i=0; i < root1Leaf.length; i++) {
    if (root1Leaf[i] != root2Leaf[i]) {
      return false
    }
  }
  return true
};
var traversal = (node, arr) => {
  if (!node) {
    return ;
  } 
  if (!node.left && !node.right) {
    arr.push(node.val)
  }
  traversal(node.left, arr)
  traversal(node.right, arr)
}