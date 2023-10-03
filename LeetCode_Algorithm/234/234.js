function ListNode(val, next){
  this.val = (val===undefined ? 0 : val)
  this.next = (next===undefined ? null : next)
}
var isPalindrome = function(head) {

  var headNode = makeTree(head, 0)
  //sol1 O(n), O(n) 156~173ms 88~77%
  // var q =[]
  // q.push(headNode)
  // ans = []
  // // console.log(q)
  // while (q) {
  //   let node = q.pop(0)
  //   if (node == undefined){break;}
  //   if (node.next != undefined) {q.push(node.next)}
  //   ans.push(node.val)
  // }
  // for (let idx=0; idx < parseInt(ans.length/2); idx++){
  //   if (ans[idx] != ans[ans.length-1-idx]){
  //     return false
  //   }
  // }
  // return true


  // sol2 O(n), O(1) 162~241ms 85~33%
  var firstHalfEnd = endOfFirstHalf(headNode)
  var secondHalfStart = reverseList(firstHalfEnd.next)

  var firstPosition = headNode
  var secondPosition = secondHalfStart
  console.log(firstPosition)
  console.log(secondPosition)
  while (secondPosition != undefined){
    if (firstPosition.val != secondPosition.val){
      // console.log(firstPosition.val, secondPosition.val)
      return false
    }
    firstPosition = firstPosition.next
    secondPosition = secondPosition.next
  }
  return true
};  
function makeTree(head, idx){
  var headNode = new ListNode(head[idx])
  if(idx+1 < head.length){
    headNode.next = makeTree(head, idx+1)
  }
  return headNode
}
function endOfFirstHalf(node){
  var fast = node
  var slow = node

  while (fast.next != undefined && fast.next.next != undefined){
    fast = fast.next.next
    slow = slow.next
  }
  return slow
}
function reverseList(node){
  let prev = null
  let curr = node

  while (curr != undefined){
    let next = curr.next
    curr.next = prev
    prev = curr
    curr = next
  }
  return prev
}


console.log(isPalindrome([1,2,2,1]));