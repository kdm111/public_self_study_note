var solve = (n, src, dest, seen, hashMap) => {
  if (n < 0) {
    return false
  }
  if (src == dest) {
    return true
  }
  for (let i of hashMap[src]) {
    if (seen.has(i)) {
      continue
    }
    n -= 1
    seen.add(i)
    if (solve(n, i, dest, seen, hashMap)) {
      return true
    }
    n += 1
  }
  return false
}
var validPath = function(n, edges, source, destination) {
  // sol1 817ms 54% 155.6MB 57%
  // process exited with signal SIGSEGV
  let hashMap = {}
  for (let edge of edges) {
    if (hashMap[edge[0]]) {
      hashMap[edge[0]].push(edge[1])
    } else {
      hashMap[edge[0]] = [edge[1]]
    }
    if (hashMap[edge[1]]) {
      hashMap[edge[1]].push(edge[0])
    } else {
      hashMap[edge[1]] = [edge[0]]
    }
  }
  let seen = new Set([source])
  return solve(n, source, destination, seen, hashMap) ? true : false
};