var coordinateToSeen = (r, c) => {
  return (String(r) + ',' + String(c))
}
var nearestExit = function(maze, entrance) {
  // sol1 195ms 33% 56.4MB 23%
  let seen = new Set()
  let temp = [...entrance]; temp.push(0)
  let queue = new Array(); queue.push(temp)
  let directions = [[0,1], [1,0], [0, -1], [-1, 0]]
  while (queue.length) {
    [r, c, k]= queue.shift()
    if (seen.has(coordinateToSeen(r,c)))
      continue
    if (!(r == entrance[0] && c == entrance[1])) {
      if (r == 0 || r == maze.length-1)
        return k
      if (c == 0 || c == maze[0].length-1)
        return k
    }
    seen.add(coordinateToSeen(r, c))
    for (let [dr, dc] of directions) {
      let nR = r + dr; let nC = c + dc
      if (0 <= nR && nR < maze.length && 0 <= nC && nC < maze[0].length) {
        if (maze[nR][nC] == '.')
          queue.push([nR, nC, k+1])
      }
    }
  }
  return -1
};