function Node(val, children) {
   this.val = val;
   this.children = []
};

function solve(root, ans) {
  if (!root) {
    return ans
  }
  ans.push(root.val)
  for (let child of root.children) {
    solve(child, ans)
  }
  return ans
};

var preorder = function() {
  // O(n) 91ms 82%
  rootNode = new Node(1)
  aNode = new Node(2); bNode = new Node(3); cNode = new Node(4);
  rootNode.children.push(aNode);
  rootNode.children.push(bNode);
  rootNode.children.push(cNode);

  return solve(rootNode, [])
};

console.log(preorder())