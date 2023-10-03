function isEqual (temp, loc) {

  return ((temp[0] == loc[0]) && (temp[1] == loc[1]))
}
function isInRechable(reachable, loc) {
  if (reachable.length == 0) {return false}
  for (let temp of reachable) {

    if (isEqual(temp, loc)) {
      return true
    }
  }
  return false
}

function dfs(ocean, heights) {
  let reachable = []
  while (ocean.length > 0) {
    let loc = ocean.pop()
    let r = loc[0]; let c = loc[1]
    if (isInRechable(reachable, loc)) {
      continue;
    }
    reachable.push(loc)
    for (let [dr, dc] of [[0,1], [1,0], [0,-1], [-1,0]]) {
      let newR = r+dr; let newC = c+dc;
      if(-1 < newR && newR < heights.length && -1 < newC && newC < heights[0].length) {
        if (heights[r][c] < heights[newR][newC] || heights[r][c] == heights[newR][newC]) {
          ocean.push([newR, newC])
        }
      }
    }
  }
  return reachable
}

var pacificAtlantic = function(heights) {
  if (!heights) {return []}
  pacificOcean = new Array(); atlanticOcean = new Array()
  for (let i in heights) {
    pacificOcean.push([parseInt(i),0]); atlanticOcean.push([parseInt(i),heights.length-1])
  }
  for (let i in heights[0]) {
    pacificOcean.push([0,parseInt(i)]); atlanticOcean.push([heights[0].length-1, parseInt(i)])
  }
  let pacificOceanArray = new Set(pacificOcean); 
  let atlanticOceanArray = new Set(atlanticOcean);
  pacificOceanArray = [...pacificOceanArray]
  atlanticOceanArray = [...atlanticOceanArray]
  
  let pacific = dfs(pacificOceanArray, heights)
  let atlantic = dfs(atlanticOceanArray, heights)
  
  let ans = []
  for (let pac of pacific) {
    for (let atl of atlantic) {
      if (isEqual(pac, atl)){
        ans.push(pac)
      }
    }
  }
  return ans.sort(function(a,b) {
    if (a[0]==b[0]){return a[1]-b[1]}
    return a[0]-b[0]
  })
};

console.log(pacificAtlantic([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]))