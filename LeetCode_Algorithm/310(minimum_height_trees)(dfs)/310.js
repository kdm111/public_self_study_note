var findMinHeightTrees = function(n, edges) {
  // 151ms 99%
  if (n < 3) {
    let ans = []
    for (let i=0; i < n; i++) {
      ans.push(i)
    }
    return ans
  }
  let adj = []
  for (let i=0; i < n; i++) {
    adj.push(new Set())
  }

  for (let [i,j] of edges) {
    adj[i].add(j)
    adj[j].add(i)
  }
  let leaves = []
  for (let i in adj) {
    if (adj[i].size == 1){
      leaves.push(i)
    }
  }
  while (n > 2) {
    n -= leaves.length
    let newLeaves = []
    for (let i of leaves) {
      let j = Array.from(adj[i]).pop()
      adj[j].delete(parseInt(i))
      if (adj[j].size == 1) {newLeaves.push(j)}
    }
    leaves = newLeaves
  }
  return leaves
};
console.log(findMinHeightTrees(4,[[1,0],[1,2],[1,3]]))


