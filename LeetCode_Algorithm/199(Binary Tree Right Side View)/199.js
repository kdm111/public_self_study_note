var rightSideView = function(root) {
  // sol1 O(n) O(n) 119ms 13%
  // if (root == null) {return []}
  // let ans = []
  // let stack = [[root]]
  // while (stack.length > 0) {
  //   let nodes = stack.shift()
  //   if (nodes == undefined || nodes.length == 0) {
  //     break
  //   }
  //   let temp = []
  //   for (let node of nodes) {
  //     if (node == null) {
  //       continue
  //     }
  //     temp_val = node.val
  //     if (node.left != null) {
  //       temp.push(node.left)
  //     }
  //     if (node.right != null) {
  //       temp.push(node.right)
  //     }
  //   }
  //   ans.push(temp_val)
  //   stack.push(temp)
  // }
  // return ans

  // sol2 63ms 83% 43.2MB 92%
  if (!root)
    return []
  let ans = []
  let queue = [root]
  while (queue.length) {
    let l = queue.length
    let val = queue[0].val
    for (let i = 0 ;i < l; i++) {
      let node = queue.shift()
      val = node.val
      if (node.left) {
        queue.push(node.left)
      }
      if (node.right) {
        queue.push(node.right)
      }
    }
    ans.push(val)
  }
  return ans
};