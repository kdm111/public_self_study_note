var reverseKGroup = function(head, k) {
  // 127ms 36%
  let cnt = 0; let node = head
  while (node && cnt < k) {
    node = node.next
    cnt++
  }
  if (cnt < k) {return head}
  temp = reverseLinkdedList(head, k)
  let newHead = temp[0]; let prev = temp[1]
  head.next = reverseKGroup(newHead, k)
  return prev
};

function reverseLinkdedList(head, cnt) {
  let prev = null; let curr = head; let next = head
  while (cnt > 0) {
    next = curr.next
    curr.next = prev
    prev = curr
    curr = next
    cnt -= 1
  }
  return [curr, prev]
}


