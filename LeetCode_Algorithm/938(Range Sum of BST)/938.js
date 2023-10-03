function TreeNode(val, left, right) {
  this.val = (val===undefined ? 0 : val)
  this.left = (left===undefined ? null : left)
  this.right = (right===undefined ? null : right)
 }

var rangeSumBST = function(root, low, high) {
  // sol1 240ms
  rootNode = makeTree(root, 0)
  preorderTraversal(rootNode)

  // var q = []
  // q.push(rootNode)
  // var ans = 0
  // while (q.length > 0){
  //   let node = q.pop(0)

  //   if (node != null) {
  //     if (low <= node.val && node.val<= high){
  //       ans += node.val
  //     }
  //     if (low < node.val){
  //       q.push(node.left)
  //     }
  //     if (node.val < high){
  //       q.push(node.right)
  //     }
  //   }
  // }
  // return ans
};

function makeTree(root, idx){
  if (idx > root.length){return}

  let rootNode = new TreeNode(root[idx])
  if(2*idx+1 < root.length){ rootNode.left = makeTree(root, 2*idx+1) }
  if(2*idx+2 < root.length){ rootNode.right = makeTree(root, 2*idx+2) }
  return rootNode
}
function preorderTraversal(node){
  if (node == null){ return }
  // console.log()를 대신하는 함수로 개행을 하지 않는다.
  // console.log = function (d){
    //   process.stdout.write(d + '\n')
    // };
  process.stdout.write(node.val + " ")
  // console.log(node.val)
  preorderTraversal(node.left)
  preorderTraversal(node.right)
}





console.log(rangeSumBST([10,5,15,3,7,null,18], 7, 15))