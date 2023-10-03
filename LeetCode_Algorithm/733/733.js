function check(visited, newX, newY) {
  var checkX = false
  var checkY = false

  for (let v of visited) {
    if (newX == v[0] && newY == v[1]) {
      return false
    }
  }
  return true
}

var floodFill = function(image, sr, sc, newColor) {
  // O(n) 145ms 9%
  var color = image[sr][sc]
  image[sr][sc] = newColor
  var visited = new Array(); visited.push([sr,sc])
  var q = new Array(); q.push([sr,sc])
  
  dr = [0,-1,0,1]; 
  dc = [1,0,-1,0]


  while (q.length > 0) {
    var arr = q.shift()
    let x = arr[0]; let y = arr[1]

    for (let i=0; i < 4; i++) {
      let newX = x+dr[i]; let newY = y+dc[i];
      if (0 <= newX && newX < image.length && 0 <= newY && newY < image[0].length) {
        if (check(visited, newX, newY)) {
          if (image[newX][newY] == color) {
            image[newX][newY] = newColor
            q.push([newX, newY])
          }
          visited.push([newX, newY])
        }
      }
    }
  }
  return image
};
// console.log(floodFill([[0,0,0],[0,1,1]], 1, 1, 1))
console.log(floodFill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2))
