var setKey = (arr) => {
  let key = ""
  for (let num of arr) {
    key += String(num) + ','
  }
  return key
}
var equalPairs = function(grid) {
  // sol1 189ms 48% 60MB 21%
  let cnt = new Map()
  for (let r=0; r < grid.length; r++) {
    cnt.set(setKey(grid[r]), (cnt.get(setKey(grid[r])) || 0) + 1)   
  }
  let ans = 0
  for (let c = 0; c < grid[0].length; c++) {
    temp = []
    for (let r=0; r < grid.length; r++) {
      temp.push(grid[r][c])
    }
    if (cnt.has(setKey(temp))) 
      ans += cnt.get(setKey(temp))
  }
  return ans
};