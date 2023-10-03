var minReorder = function(n, connections) {
  // sol1 613ms 37% 82.1MB 71%1
  let hashMap = new Map()
  let seen = new Set()
  let roads = new Set();
  for (let i = 0; i < n; i++) {
    hashMap.set(i, [])
  }
  for (let [i,j] of connections) {
    hashMap.get(i).push(j)
    hashMap.get(j).push(i)
    roads.add(String(i) + "," + String(j))
  }
  seen.add(0)
  let dfs = (node) => {
    let ans = 0
    for (let i of hashMap.get(node)) {
      if (!seen.has(i)) {
        if (roads.has(String(node) + ',' + String(i))) {
          ans += 1
        }
        seen.add(i)
        ans += dfs(i)
      }
    }
    return ans
  }
  return dfs(0)
};