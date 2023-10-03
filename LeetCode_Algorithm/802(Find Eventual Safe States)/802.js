var dfs = (i, graph) => {
  if (visited[i] == 1) {
    return true
  } else if (visited[i] == -1) {
    return false
  }
  visited[i] = -1
  for (let n of graph[i]) {
    if(!dfs(n, graph)) {
      return false
    }
  }
  visited[i] = 1
  return true
}

var eventualSafeNodes = function(graph) {
  // sol1 119ms 87% 51.4MB 71%
  visited = new Array(graph.length).fill(0)
  let ans = []
  for (let i = 0; i < graph.length; i++) {
    if (dfs(i, graph)) {
      ans.push(i)
    }
  }
  return ans
};

console.log(eventualSafeNodes([[1,2],[2,3],[5],[0],[5],[],[]]))