var mergeKLists = function(lists) {
  // sol1 O(nlogn) O(n) 163ms 57%
  let root = new ListNode(null)
  let ans = root
  let temp = []
  for (let node of lists) {
    while (node) {
      temp.push(node)
      node = node.next
    }
  }
  temp.sort((a, b) => {return a.val-b.val})
  for (let node of temp) {
    root.next = node
    root = root.next
  }
  return ans.next
};

console.log(mergeKLists([root1, root2, root3]))