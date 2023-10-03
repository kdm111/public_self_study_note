function ListNode(val, next) {
  this.val = (val===undefined ? 0 : val)
  this.next = (next===undefined ? null : next)
}

function makeListNode(lst, idx) {
  if (lst.length == idx) {
    return null
  }
  let root = new ListNode(lst[idx])
  root.next = makeListNode(lst, idx+1)
  return root
}

var rotateRight = function(head, k) {
  // O(n) O(1) 123ms 22%
  if (k == 0 || head == null  || head.next == null) {
    return head
  }
  let cnt = 0
  dummy = head
  while (dummy) {
    dummy = dummy.next
    cnt += 1
  }
  cnt = k % cnt
  while (cnt > 0) {
    let dummy = new ListNode(null)
    dummy.next = head
    while (head.next && head.next.next) {
      head = head.next
    }
    let prev = head; let next = head.next
    prev.next = null; next.next = dummy.next
    head = next
    cnt -= 1
  }
  return head
};

let root = makeListNode([1,2,3,4,5], 0)
console.log(rotateRight(root, 2))