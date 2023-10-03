var deleteDuplicates = function(head) {
  // sol2 123ms 28%
  if (!head) {
    return head
  }  
  let prev = head; let curr = head.next

  while (curr) {
    if (prev.val == curr.val) {
      curr = curr.next
      prev.next = curr
    } else{
      prev = curr
      curr = curr.next
    }
  }
  return head
};