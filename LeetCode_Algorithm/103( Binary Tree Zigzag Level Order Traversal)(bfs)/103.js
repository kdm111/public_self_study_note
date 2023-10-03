
var zigzagLevelOrder = function(root) {
  // 112ms 23%
  // if (root == undefined) {
  //   return []
  // }  
  // let ans = [[root.val]]
  // let queue = [root]
  // while (queue.length > 0) {
  //   let temp_queue = []; let temp_ans = []
  //   while (queue.length > 0) {
  //     node = queue.shift()
  //     if (node && node.left) {
  //       temp_ans.push(node.left.val)
  //       temp_queue.push(node.left)
  //     }
  //     if (node && node.right) {
  //       temp_ans.push(node.right.val)
  //       temp_queue.push(node.right)
  //     }
  //   }
  //   if (ans.length % 2 == 1) {
  //     temp_ans.reverse()
  //   }
  //   if (temp_ans.length > 0) {
  //       ans.push(temp_ans)
  //   }
  //   queue = temp_queue
  // }
  // return ans 

  // sol2 57ms 97% 42.3MB 99%
  if (!root)
    return []
  let ans = []
  let queue = [root]; let depth = 0
  while (queue.length) {
    let temp = []; let l = queue.length
    for (let i = 0; i < l; i++) {
      let node = queue.shift()
      temp.push(node.val)
      if (node.left) {
        queue.push(node.left)
      }
      if (node.right) {
        queue.push(node.right)
      }
    }
    if (depth % 2)
      temp.reverse()
    depth += 1
    ans.push(temp)
  }
  return ans
};