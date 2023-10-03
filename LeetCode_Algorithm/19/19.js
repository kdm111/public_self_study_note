
 function ListNode(val, next) {
     this.val = (val===undefined ? 0 : val)
     this.next = (next===undefined ? null : next)
 }
 function makeTree(root, idx) {
  const rootNode = new ListNode(root[idx])
  if (idx+1 < root.length) {
    rootNode.next = makeTree(root, idx+1)
  }
  return rootNode
 }
var removeNthFromEnd = function(head, n) {
  // O(n) O(1) 89ms 54%
  head = makeTree(head, 0)  
  const dummy = new ListNode(null); dummy.next = head
  let lenNode = dummy; let length = 0
  while (lenNode.next) {
    lenNode = lenNode.next
    length += 1
  }
  length -= n
  let first = dummy
  while (length > 0) {
    first = first.next
    length -= 1
  }
  first.next = first.next.next
  return dummy.next

};

console.log(removeNthFromEnd([1,2,3,4,5], 2))