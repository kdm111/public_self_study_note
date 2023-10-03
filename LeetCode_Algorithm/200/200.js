function check(visited, r, c) {
  for (let arr of visited) {
    if (arr[0] == r && arr[1] == c){
      return false
    }
  }
  return true
}
function solve(grid, r, c, visited) {
  // O(n) O(n) 5432ms 5%
  grid[r][c] = '0'
  dr = [0, 1, 0, -1]
  dc = [1, 0, -1, 0]

  for (let i=0; i < 4 ; i++) {
    let newR = r+dr[i]; let newC = c+dc[i]
    if (0 <= newR && newR < grid.length && 0 <= newC && newC < grid[0].length) {
      if(grid[newR][newC] == '1' && check(visited, newR, newC)){
        solve(grid, newR, newC, visited)
      }
      visited.push(newR, newC)
    }
  }
}
var numIslands = function(grid) {
  var ans = 0
  var visited = []
  for (let c in grid[0]) {
    for (let r in grid) {
      if (grid[r][c] == "1") {
        ans += 1
        solve(grid, parseInt(r), parseInt(c), visited)
      }
    }
  }
  return ans
};

console.log(numIslands(
  [["1","1","1","1","0"],
    ["1","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]]))
