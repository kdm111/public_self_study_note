var possible = function(bomb1, bomb2) {
  [x1, y1, r1] = [...bomb1]; [x2, y2, r2] = [...bomb2]
  dist = Math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
  return r1 >= dist
}
var maximumDetonation = function(bombs) {
  // sol1 341ms 42% 48.7MB 90%
  connected = new Array(bombs.length)
  for (let i = 0; i < bombs.length; i++) {
    connected[i] = new Set()
  }

  for (let i = 0; i < bombs.length; i++) {
    for (let j = 0; j < bombs.length; j++) {
      if (i != j && possible(bombs[i], bombs[j])) {
        connected[i].add(j)
      }
    }
  }
  console.log(connected)
  let ans = 0
  for (let i = 0; i < connected.length; i++) {
    let seen = new Set()
    dfs(i, seen)
    ans = Math.max(ans, seen.size)
  }
  return ans
};

var dfs = function(i, seen) {
  seen.add(i)
  for (let node of connected[i]) {
    if (!seen.has(node)) {
      dfs(node, seen)
    }
  }
}

console.log(maximumDetonation([[1,1,5],[10,10,5]]))