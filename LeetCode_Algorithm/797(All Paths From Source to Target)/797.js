var dfs = (graph, idx, temp, goal) => {
  if (idx == goal) {
    ans.push(temp.slice(0, ))
    return ;
  }
  for (let k of graph[idx]) {
    temp.push(k)
    dfs(graph, k, temp, goal)
    temp.pop()
  }
}
var allPathsSourceTarget = function(graph) {
  // sol1 87ms 99% 48.3MB 96%
  ans = []
  dfs(graph, 0, [0], graph.length-1)
  return ans  
};

console.log(allPathsSourceTarget([[1,2],[3],[3],[]]))
console.log(allPathsSourceTarget([[4,3,1],[3,2,4],[3],[4],[]]))
