var reachableNodes = function(n, edges, restricted) {
  // sol1 583ms 51% 103MB 89%
  var valid = (node) => {
    return (!restrictedSet.has(node)) && (!seen.has(node))
  }
  let graph = new Map()
  for (let i = 0; i < n; i++) {
    graph.set(i, [])
  }
  for (let [i, j] of edges) {
    let val = graph.get(i); val.push(j)
    graph.set(i, val)
    val = graph.get(j); val.push(i)
    graph.set(j, val)
  }
  let restrictedSet = new Set(restricted); let seen = new Set()
  let ans = 0; let stack = [0]
  while (stack.length) {
    node = stack.pop()
    ans += 1
    seen.add(node)
    let val = graph.get(node)
    for (let n of val) {
      if (valid(n))
        stack.push(n)
    }
  }
  return ans
};

console.log(reachableNodes(7, [[0,1],[1,2],[3,1],[4,0],[0,5],[5,6]], [4,5]))