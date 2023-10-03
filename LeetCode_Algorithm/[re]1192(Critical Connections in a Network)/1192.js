var dfs = function(prevNode, currNode, currDepth) {
  rank[currNode] = currDepth
  minDepth = currDepth
  for (let node of hashMap[currNode]) {
    if (prevNode == node) {
      continue
    }
    temp = rank[node]
    if (temp == -1) {
      temp = dfs(currNode, node, currDepth+1)
    }
    console.log(prevNode, currNode, node, temp)
    if (temp > currDepth) {
      ans.push([currNode, node])
    } else {
      minDepth = Math.min(minDepth, temp)
    }
  }
  rank[currNode] = minDepth
  return rank[currNode]
}
var criticalConnections = function(n, connections) {
  // sol1
  hashMap = new Map()
  for (let i=0; i < n; i++) {
    hashMap[i] = new Set()
  }
  for (let [i,j] of connections) {
    hashMap[i].add(j)
    hashMap[j].add(i)
  }
  rank = new Array(n).fill(-1)
  ans = []
  dfs(null, 0, 0)
  console.log(rank)
  return ans
};

console.log(criticalConnections(4, [[0,1],[1,2],[2,0],[1,3]]))