var findMinArrowShots = function(points) {
  // sol2 201ms 100% 74.6MB 64%
  points.sort((a,b) => {
    return a[1] - b[1]
  })
  let maxX = points[0][1]; let ans = 1
  for (let i = 1; i < points.length; i++) {
    if (maxX >= points[i][0]) {
      continue
    }
    ans += 1
    maxX = points[i][1]
  }
  return ans
};

console.log(findMinArrowShots([[10,16],[2,8],[1,6],[7,12]]))