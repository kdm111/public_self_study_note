var makeConnected = function(n, connections) {
  // sol1 351ms 31%
  if (connections.length < n-1) {return -1}
  hashMap = new Map()
  for (let [i,j] of connections) {
    if (hashMap[i] == undefined) {
      hashMap[i] = [j]
    } else {
      hashMap[i].push(j)
    }
    if (hashMap[j] == undefined) {
      hashMap[j] = [i]
    } else {
      hashMap[j].push(i)
    }
  }
  for (let k=0; k < n; k++) {
    if(hashMap[k] == undefined) {
      hashMap[k] = []
    }
  }
  visited = new Set()
  let ans = 0
  for (let k=0; k < n; k++) {
    if (!visited.has(k)) {
      dfs(k); ans++
    }
  }
  return ans-1
};

var dfs = function(k) {
  visited.add(k)
  for (let node of hashMap[k]) {
    if (!visited.has(node)) {
      dfs(node)
    }
  }
}
console.log(makeConnected())