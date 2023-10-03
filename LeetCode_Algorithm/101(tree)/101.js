var isSymmetric = function(root) {
  // sol1 O(n) O(1) 89ms 69%
  
  let lst = new Array([root, root])
  while (lst.length > 0) {
    temp = lst.shift()
    let p = temp[0]; let q = temp[1]
    if (p == null && q == null) {
      continue
    } else if (!p || !q) {
      return false
    } else if (p.val != q.val){
      return false
    }
    lst.push([p.left, q.right])
    lst.push([p.right, q.left])
  }
  return true
};
