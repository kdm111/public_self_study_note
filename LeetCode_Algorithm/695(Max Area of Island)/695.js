var dfs = function(grid, r, c) {
    if (0 <= r && r < grid.length && 0 <= c && c < grid[0].length) {
        if (grid[r][c] == 1) {
            // js에서 다양한 값을 체크하는 대신에 기존의 대지를 방문 불가능으로 만들어 체크
            grid[r][c] = -1
            let ret = 1
            for (let i=0; i < 4; i++) {
                ret += dfs(grid, r+dr[i], c+dc[i])
                console.log(r,c,ret)
            }
            return ret
        }
    }
    return 0;
}
var maxAreaOfIsland = function(grid) {
  // sol1 442ms 5%
  // O(mn) O(mn)
//   dr = [0,1,0,-1]
//   dc = [1,0,-1,0]
//   ans = 0
//   for (let r =0; r < grid.length; r++) {
//     for (let c=0; c < grid[0].length; c++) {
//         if (grid[r][c] == 1) {
//             ans = Math.max(ans, dfs(grid, r,c))
//         }
//     }
//   }
//   return ans

    // sol2 98ms 40% 49.2MB 21%
    var valid = (r, c) => {
        let rCheck = (0 <= r && r < grid.length)
        let cCheck = (0 <= c && c < grid[0].length)
        if (!(rCheck && cCheck))
            return false
        let landCheck = (grid[r][c] == 1)
        let seenCheck = !(seen.has(String(r) + ',' + String(c)))
        return landCheck && seenCheck
    }
    let directions = [[0,1], [1,0], [0, -1], [-1, 0]]
    let seen = new Set(); let ans = 0
    for (let r = 0; r < grid.length; r++) {
      for (let c = 0; c < grid[0].length; c++) {
        if (valid(r, c)) {
          seen.add(String(r) + ',' + String(c))
          let stack = [[r,c]]; let temp = 0
          while (stack.length) {
            [valid_r, valid_c] = stack.pop()
            temp += 1
            for (let i = 0 ; i < 4; i++) {
              let newR = valid_r + directions[i][0]
              let newC = valid_c + directions[i][1]
              if (valid(newR, newC)) {
                seen.add(String(newR) + ',' + String(newC))
                stack.push([newR, newC])
              }
            }
          }
          ans = Math.max(ans, temp)
        }
      }
    }
    return ans
};
[[0,0,1,0,1,1,1,0],
 [1,0,0,0,1,0,1,0],
 [0,0,1,1,0,0,1,0],
 [1,1,1,1,0,1,1,0],
 [1,1,0,1,1,0,1,0]]


console.log(maxAreaOfIsland([[0,0,1,0,1,1,1,0],[1,0,0,0,1,0,1,0],[0,0,1,1,0,0,1,0],[1,1,1,1,0,1,1,0],[1,1,0,1,1,0,1,0]]
  ))