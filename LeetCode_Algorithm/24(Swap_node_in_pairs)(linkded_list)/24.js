function ListNode(val, next) {
  this.val = val===undefined ? null : val
  this.next = next===undefined ? null : next
}
var swapPairs = function(head) {
  // sol1 O(n) O(1)
  // 63ms 91%

  let prev = new ListNode(null); prev.next = head
  let ans = prev

  while (head && head.next) {
    let first = head; let second = head.next
  
    prev.next = second
    first.next = second.next
    second.next = first
  
    prev = first
    head = first.next
  }
  return ans.next
};


console.log(swapPairs(head))