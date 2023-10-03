
function TreeNode(val, left, right) {
  this.val = (val===undefined ? 0 : val)
  this.left = (left===undefined ? null : left)
  this.right = (right===undefined ? null : right)
}
class Queue{
  constructor(){
    this.queue = []
  } 
  enqueue(item){
    this.queue.push(item)
  }
  dequeue(){
    return this.queue.shift()
  }
}
var isSymmetric = function(root) {
  var rootNode = makeTree(root, 0)
  //return checkLeftRight(rootNode, rootNode)

  // sol2 87~118ms 64~21%
  q = new Queue()
  q.enqueue(rootNode); q.enqueue(rootNode)
  while (q.queue.length > 0){
    left = q.dequeue()
    right = q.dequeue()
    if (left == undefined && right == undefined) {continue}
    if (left == undefined || right == undefined) {return false}
    if (left.val != right.val) {return false}
    q.enqueue(left.left); q.enqueue(right.right)
    q.enqueue(left.right); q.enqueue(right.left)
  }
  return true

};
// sol1 O(n), O(n) 84~118ms 68~21% 
// function checkLeftRight(left, right){
//   if (left == undefined && right == undefined) { return true }
//   if (left == undefined || right == undefined) { return false }
//   if (left.val != right.val) {return false}
//   return (checkLeftRight(left.left, right.right) && checkLeftRight(left.right, right.left))
// }
function makeTree(root, idx){
  var rootNode = new TreeNode(root[idx])
  if (2*idx+1 < root.length){rootNode.left = makeTree(root, 2*idx+1)}
  if (2*idx+2 < root.length){rootNode.right = makeTree(root, 2*idx+2)}
  return rootNode

}

console.log(isSymmetric([1,2,2,null,3,null,3]))