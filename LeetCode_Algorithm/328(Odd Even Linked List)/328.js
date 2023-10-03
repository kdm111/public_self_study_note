function ListNode(val, next) {
  this.val = (val===undefined ? 0 : val)
  this.next = (next===undefined ? null : next)
}
function makeTree(head, idx) {
  var root = new ListNode(head[idx])
  console.log(root.val)
  if (idx +1 < head.length) {
    root.next = makeTree(head, idx+1)
  }
  return root
}
var oddEvenList = function(head) {
  // O(n) O(1) 91ms 68%
  // var head = makeTree(head, 0)
  // var oddhead = new ListNode(null); var evenhead = new ListNode(null)
  // var odd = oddhead; var even = evenhead
  // let c = 1
  // while (head != undefined) {
  //   if (c % 2 == 1){
  //     odd.next = head
  //     odd = odd.next
  //   }
  //   else {
  //     even.next = head
  //     even = even.next
  //   }
  //   head = head.next
  //   c += 1
  // }
  // even.next= null
  // odd.next= evenhead.next
  // return oddhead.next

  // sol2 65ms 88% 43.99ㅡㅠ 97%
  if (!head || !head.next) {
    return head
  }
  let odd = head
  let even = head.next; let middle = head.next
  while ((odd && odd.next) && (even && even.next)) {
    let oddTemp = odd.next.next
    let evenTemp = even.next.next
    odd.next = oddTemp
    even.next = evenTemp
    odd = odd.next
    even = even.next
  }
  if (even)
    even.next = null
  odd.next = middle
  return head

};

console.log(oddEvenList([1,2,3,4,5]))
