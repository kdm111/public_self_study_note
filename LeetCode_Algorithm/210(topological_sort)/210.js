function dfs(i) {

  if (visited[i] == 1) {
    findCycle = 1; return
  }
  if (visited[i] == 0) {
    visited[i] = 1
    for (let num of map[i]){
      dfs(num)
    } 
    visited[i] = 2
    ans.push(i)
  }
}

var findOrder = function(numCourses, prerequisites) {
  // sol1 234ms 11%
  map = new Map()
  for (let num=0; num < numCourses; num++) {
    map[parseInt(num)] = []
  }
  for (let req of prerequisites) {
    map[req[1]].push(req[0])
  }
  console.log(map)
  visited = new Array(numCourses).fill(0)
  findCycle = 0
  ans = []
  for (let num=0; num < numCourses; num++) {
    if (findCycle == 1) {break}
    if (visited[num] == 0) {
      dfs(num)
    }
  }
  return findCycle == 1 ? [] : ans.reverse()
  
};

console.log(findOrder(4, [[1,0],[2,0],[3,1],[3,2]]))
console.log(findOrder(2, [[1,0], [0,1]]))