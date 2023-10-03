var orangesRotting = function(grid) {
  // O(n) O(1) 426ms 5%
  let freshOrange = 0;
  let minute = 0;
  let rotten_location = []
  const dr = [0,-1,0,1]; const dc = [1,0,-1,0]
  for (let r in grid) {
    for (let c in grid[0]){
      if (grid[r][c] == 1){
        freshOrange += 1
      } else if (grid[r][c] == 2) {
        rotten_location.push([r,c])
      }
    }
  }
  while (true) {
    let temp = []
    while (rotten_location.length > 0) {
      [r,c] = rotten_location.pop()
      for (let i=0; i < 4; i++) {
        let newR = parseInt(r) + dr[i]; let newC = parseInt(c) + dc[i]
        console.log(newR, newC)
        if (-1 < newR && newR < grid.length && -1 < newC && newC < grid[0].length) {
          if (grid[newR][newC] == 1) {
            console.log(newR, newC)
            freshOrange -= 1; grid[newR][newC] = 2; temp.push([newR,newC])
          }
        }
      }
    }
    minute += 1
    // console.log(temp, minute)
    if (temp.length == 0) {
      break;
    }
    rotten_location = temp
  }
  if (freshOrange > 0) {
    return -1
  }
  return minute-1
};

// console.log(orangesRotting([[2,1,1],[1,1,0],[0,1,1]]))
console.log(orangesRotting([[1,2]]))
