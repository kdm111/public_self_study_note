function ListNode(val, next) {
  this.val = (val===undefined ? 0 : val)
  this.next = (next===undefined ? null : next)
}

var deleteDuplicates = function(head) {
  // 61ms 84% 44.5MB 29%
  if (!head || !head.next) {
    return head
  }
  let prev = new ListNode(0); let ans = prev
  let curr = head; let next = head.next
  while (next) {
    if (curr.val != next.val) {
      prev.next = curr; prev = prev.next
      curr = next; next = next.next
    } else {
      while (next && curr.val == next.val)
        next = next.next
      curr = next
      next = next.next
    }
  }  
  prev.next = curr
  return ans.next
};