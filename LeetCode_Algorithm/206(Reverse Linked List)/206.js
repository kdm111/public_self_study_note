 function ListNode(val, next) {
     this.val = (val===undefined ? 0 : val)
     this.next = (next===undefined ? null : next)
 }

var reverseList = function(head) {
  // sol1 O(n), O(1) 56~76ms 99~70%
  if (head == null) {return null}
  if (head.next == undefined){return head}
  var root = makeTree(head, 0)
  
  var curr = root.next
  var prev = root
  prev.next = null
  while (curr != null) {
    var temp = curr.next
    curr.next = prev
    prev = curr
    curr = temp
  }
  return prev
};
var makeTree = function(head, idx){
  var rootNode = new ListNode(head[idx])
  if(idx+1<head.length){rootNode.next = makeTree(head, idx+1)}
  return rootNode
}
console.log(reverseList([]))