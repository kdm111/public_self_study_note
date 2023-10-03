var connect = function(root) {
  // sol1 128ms 45%
  if (!root) {
    return root
  }  
  let leftMost = root
  while (leftMost.left) {
    let head = leftMost
    while (head) {
        head.left.next = head.right
        if (head.next) {
            head.right.next = head.next.left
        }
        head = head.next
    }
    leftMost = leftMost.left
  }
  return root
};