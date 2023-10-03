var findSmallestSetOfVertices = function(n, edges) {
  // sol1 214ms 38% 69.9MB 42.8%
  let nodes = new Set(new Array(n).fill(0).map((_, i) => i))
  for (let [_, node] of edges) {
    if (nodes.has(node)) {
      nodes.delete(node)
    }
  }
  return Array.from(nodes)
};
console.log(findSmallestSetOfVertices(6, [[]]))