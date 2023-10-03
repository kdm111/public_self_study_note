var solve1 = function(pid, ppid, kill) {
  ans.add(kill)
  for (let idx=0; idx < ppid.length; idx++) {
    if (ppid[idx] == kill) {
      solve1(pid, ppid, pid[idx])
    }
  }
}
var solve2 = function(map, kill) {
  ans.add(kill)
  let idx = String(kill)
  if (!map[idx]) {
    return 
  }
  for (let num of map[idx]) {
    solve2(map, num)
  }
}
var killProcess = function(pid, ppid, kill) {
  // sol1 4228ms 5%
  // dfs
  // ans = new Set()
  // solve1(pid, ppid, kill)
  // return Array.from(ans)


  // sol2 270ms 34%
  ans = new Set()
  let hashMap = new Map(new Array)
  for (let idx=0; idx< ppid.length; idx++) {
    if (idx < pid.length) {
      if (hashMap[ppid[idx]]) {
        hashMap[ppid[idx]].add(pid[idx])
      } else {
        hashMap[ppid[idx]] = new Set().add(pid[idx])
      }
    } else {
      hashMap[ppid[idx]] = null
    }
  }
  solve2(hashMap, kill)
  return Array.from(ans)
};



console.log(killProcess([1,3,10,5], [3,0,5,3], 5))