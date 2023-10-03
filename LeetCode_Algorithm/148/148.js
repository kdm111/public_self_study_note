function ListNode(val, next) {
  this.val = (val === undefined ? 0 : val)
  this.next = (next === undefined ? null : next)
}

function makeTree (head, idx) {
  var root = new ListNode(head[idx])
  if (idx+1 < head.length) {root.next = makeTree(head, idx+1)}
  return root
}
function merge(left, right) {
  head = new ListNode(null)
  node = head
  while (left && right) {
    if (left.val > right.val) {
      node.next= right
      right = right.next
    }
    else {
      node.next = left
      left = left.next
    }
    node = node.next
  }
  if (left) {
    node.next = left
  }
  if (right) {
    node.next = right
  }
  return head.next
  
}
var sortList = function(head) {
   // 323ms 27%
  if (!head || !head.next) {
    return head
  }
  let prev = null; let slow = head; let fast = head
  while (fast != undefined && fast.next != undefined) {
    prev = slow; slow = slow.next; fast = fast.next.next
  }
  prev.next = null
  return merge(sortList(head), sortList(slow))
};



var head = makeTree([4,1,2,3], 0)

console.log(sortList(head))
