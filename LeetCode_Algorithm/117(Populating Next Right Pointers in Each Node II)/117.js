function Node(val, left, right, next) {
  this.val = val === undefined ? null : val;
  this.left = left === undefined ? null : left;
  this.right = right === undefined ? null : right;
  this.next = next === undefined ? null : next;
};

var connect = function(root) {
  // sol2 62ms 82% 46.35MB 65%
  let node = root
  while (node) {
    let temp = new Node(0)
    let child = temp
    while (node) {
      if (node.left) {
        child.next = node.left
        child = child.next
      }
      if (node.right) {
        child.next = node.right
        child = child.next
      }
      node = node.next
    }
    node = temp.next
  }
  return root
};