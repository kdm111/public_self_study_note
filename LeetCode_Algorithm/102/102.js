function TreeNode(val, left, right) {
  this.val = (val===undefined ? 0 : val)
  this.left = (left===undefined ? null : left)
  this.right = (right===undefined ? null : right)
}

function solve(root, temp, ans) {
  if (root.length <= 0) {
    return ;
  }
  let i = 0
  const length = root.length
  let children = []
  while (i < length) {
    const node = root.shift()
    temp.push(node.val)
    if (node.left) {
      children.push(node.left)
    }
    if (node.right) {
      children.push(node.right)
    }
    i++;
  }
  ans.push(temp)
  solve(children, [], ans)
}
var levelOrder = function(root) {
  if (root == null) {return []}    
  
  // iterative
  // stack = [root]
  // ans = []
  // while (stack.length > 0) {
  //   temp = []
  //   length = stack.length
  //   for (let i=0; i < length; i++) {
  //     node = stack.shift()
  //     if (node != undefined) {
  //       temp.push(node.val)
  //     }
  //     if (node.left) {
  //       stack.push(node.left)
  //     } 
  //     if (node.right) {
  //       stack.push(node.right)
  //     }
  //   }
  //   ans.push(temp)
  // }
  // return ans

  // recursive O(n) O(n) 94ms 50%
  let ans = []
  solve([root], [], ans)
  return ans
};