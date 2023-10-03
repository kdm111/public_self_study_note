var countComponents = function(n, edges) {
  // sol1 89ms 45% 48.1MB 8%
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
  let seen = new Set(); let ans = 0
  for (let i = 0 ; i < n ; i++ ){
    if (seen.has(i))
      continue
    let stack = [i]
    while (stack.length) {
      let node = stack.pop()
      if (seen.has(node))
        continue
      seen.add(node)
      let iter = graph.get(node)
      for (let i of iter) {
        stack.push(i)
      }
    }
    ans += 1
  }
  return ans
};

console.log(countComponents(5, [[0,1],[1,2],[2,3],[3,4]]))