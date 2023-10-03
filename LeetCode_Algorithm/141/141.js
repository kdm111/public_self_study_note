function ListNode(val){
  this.val = val
  this.next = null
}
var hasCycle = function(head, pos) {
  // sol1 O(n), O(1) 79~110 82~25%
  // Floyd's cycle finding algorithm
  if (head.length < 2) {return False}  
  var rootNode = makeTree(head, 0)

  var endNode = rootNode
  while (endNode.next != null) {
    endNode = endNode.next
  }

  var idx = 0
  var returnNode = rootNode
  while (idx < pos){
    returnNode = returnNode.next
    idx += 1
  }

  endNode.next = returnNode

  // currNode = rootNode 
  // nextNode = rootNode.next

  // while (currNode != nextNode){
  //   if (nextNode == null || nextNode.next == null) {return false}
  //   currNode = currNode.next
  //   nextNode = nextNode.next.next
  // }
  // return true

  // sol2 O(n), O(n) 85~116ms 73~29%
  // map
  // seen = new Map()
  
  // while (rootNode != null){
  //   if (seen.has(rootNode)){return true}
  //   seen.set(rootNode, "")
  //   rootNode = rootNode.next
  // }
  // return false

  // sol3
  let slow = rootNode; let fast = rootNode
  while (fast && fast.next) {
    slow = slow.next
    fast = fast.next.next
    if (slow == fast) {
      return true
    }
  }
  return false
};

function makeTree(head, idx){
  let rootNode = new ListNode(head[idx])
  if (idx+1 < head.length) {rootNode.next = makeTree(head, idx+1)}
  return rootNode

}
console.log(hasCycle([3,2,0,-1],1))