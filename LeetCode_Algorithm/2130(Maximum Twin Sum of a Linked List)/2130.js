
var pairSum = function(head) {
  // sol1 181ms 72% 65.1MB 93%
  let slow = head; let fast = head
  while (fast && fast.next) {
    fast = fast.next.next
    slow = slow.next
  }    
  let prev = null
  let curr = slow
  while (curr) {
    let next = curr.next
    curr.next = prev
    prev = curr
    curr = next
  }
  let ans = 0
  while (prev) {
    ans = Math.max(ans, head.val+prev.val)
    prev = prev.next
    head = head.next
  }
  return ans
};