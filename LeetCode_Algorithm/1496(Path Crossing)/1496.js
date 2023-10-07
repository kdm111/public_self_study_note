function hashing(x, y) {
  return 10001 * x + y
}
var isPathCrossing = function(path) {
  // sol1 47ms 85% 42.1MB 53%
  let seen = new Set()
  seen.add(0)
  let x = 0; let y = 0;
  for (const direction of path) {
    if (direction == 'N') {
      y += 1
    } else if (direction == 'W') {
      x -= 1
    } else if (direction == 'S') {
      y -= 1
    } else {
      x += 1
    }
    if (seen.has(hashing(x, y))) {
      return true
    }
    seen.add(hashing(x,y))
  }
  return false
};