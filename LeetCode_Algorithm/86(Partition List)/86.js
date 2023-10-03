function ListNode(val, next) {
  this.val = (val===undefined ? 0 : val)
  this.next = (next===undefined ? null : next)
}
var partition = function(head, x) {
  // sol1 54ms 90% 43.9MB 42%
  let ans =  new ListNode(-1); let greater = new ListNode(-1) 
  let less = ans; let temp = greater

  while (head) {
    if (head.val < x) {
      less.next = head; head = head.next
      less = less.next; less.next = null 
    } else {
      greater.next = head; head = head.next
      greater = greater.next; greater.next = null
    }
  }
  less.next = temp.next
  return ans.next
};