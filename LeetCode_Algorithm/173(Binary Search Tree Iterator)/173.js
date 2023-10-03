var BSTIterator = function(root) {
  // sol1 T : 246ms 20% S : 55.6MB 62%
  this.arr = []; queue = []
  while (true) {
    if (root) {
      queue.push(root)
      root = root.left
    } else if (queue.length) {
      root = queue.pop()
      this.arr.push(root)
      root = root.right
    } else {
      break
    }
  }
  return null
};

BSTIterator.prototype.next = function() {
    if (this.arr.length) {
    let node = this.arr.shift()
    return node.val
    } else {
        return null
    }
};

BSTIterator.prototype.hasNext = function() {
  return this.arr.length > 0 ? true : false
};