function ListNode(val, next) {
    this.val = (val===undefined ? 0 : val)
    this.next = (next===undefined ? null : next)
}
var removeElements = function(head, val) {
  // sol1 140ms 30%
  let dummy = new ListNode(0);
  dummy.next = head
  prev = dummy
  curr = head
  while (curr) {
    if (curr.val == val) {
      prev.next = curr.next
    } else {
      prev = curr
    }
    curr= curr.next
  }
  return dummy.next
};