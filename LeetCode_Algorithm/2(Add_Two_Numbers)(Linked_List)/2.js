function ListNode(val, next) {
    this.val = (val===undefined ? 0 : val)
    this.next = (next===undefined ? null : next)
}

var makeListNode = function(lst, idx) {
  if (idx == lst.length) {
    return null
  }
  let rootNode = new ListNode(lst[idx])
  rootNode.next = makeListNode(lst, idx+1)
  return rootNode
}
var addTwoNumbers = function(l1, l2) {
  // sol2 192ms 22%
  let l1Root = makeListNode(l1, 0)
  let l2Root = makeListNode(l2, 0)

  let ans = new ListNode(null)
  let ansCopy = ans
  let carry = 0;
  while (l1Root|| l2Root || carry > 0) {
    let l1Val = l1Root ? l1Root.val : 0
    let l2Val = l2Root ? l2Root.val : 0

    let sum = l1Val+l2Val+carry
    carry = parseInt(sum / 10); let mod = sum % 10
    ansCopy.next = new ListNode(mod)
    ansCopy = ansCopy.next

    l1Root = l1Root ? l1Root.next : null 
    l2Root = l2Root ? l2Root.next : null
  }
  return ans.next
};


console.log(addTwoNumbers([9,9], [9]))
