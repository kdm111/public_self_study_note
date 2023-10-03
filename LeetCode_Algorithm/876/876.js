function ListNode(val, next) {
  this.val = (val===undefined ? 0 : val)
  this.next = (next===undefined ? null : val)
}
var makeTree = function(head, idx) {
  var rootNode = new ListNode(head[idx])
  if (idx+1 < head.length) {rootNode.next = makeTree(head, idx+1)}
  return rootNode
}
var middleNode = function(head) {
  var rootNode = makeTree(head, 0)
  // sol1 O(n), O(1) 70~87ms 66~37%
  //  if (rootNode.next == null) {return rootNode}
  
  //  var slow = rootNode; var fast = rootNode;
  //  while (fast != null && fast.next != null) {
  //    console.log(slow.val, fast.val)
  //    slow = slow.next
  //    fast = fast.next.next
  //  }
  //  return slow.val


  // sol2 O(n), O(n) 83~96ms 43~21%
  arr = [rootNode]
  while (arr[arr.length-1].next != null) {
    arr.push(arr[arr.length-1].next)
  }
  return arr[parseInt(arr.length/2)]
  
}
console.log(middleNode([1,2,3,4,5,6]))