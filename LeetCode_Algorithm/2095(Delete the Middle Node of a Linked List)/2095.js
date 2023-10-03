function ListNode(val, next) {
  this.val = (val === undefined ? 0 : val)
  this.next = (next == undefined ? null : next)
}

var deleteMiddle = function(head) {
  // 668ms 53% 126.1MB 68%
  if (!head || !head.next) {
    return null
  }
  let slow = head; let fast = head;
  let prev = slow;
  while (fast && fast.next) {
    prev = slow
    slow = slow.next
    fast = fast.next.next
  }
  prev.next = slow.next
  return head
};