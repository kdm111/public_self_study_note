var binarySearch = function(map, idx) {
  let left = 0; let right = map.length-1
  while (left < right || left == right) {
    let mid = parseInt((left+right)/2)
    if (map[mid] == idx) {
      return mid
    }
    if (map[mid] > idx) {
      right = mid-1
    } else {
      left = mid+1
    }
  }
  return left
}
var shortestDistanceColor = function(colors, queries) {
  // sol3 594ms 43%
  // mid값을 찾아서 최소 값을 찾아냄
  let hashMap = new Map()
  for (let [idx, color] of colors.entries()) {
    if (hashMap[color] == undefined) {
      hashMap[color] = [idx]
    } else {
      hashMap[color].push(idx)
    }
  }
  let ans = []
  for (let query of queries) {
    let idx = query[0]; let color = query[1]
    if (hashMap[color] == undefined) {
      ans.push(-1)
    } else {
      let map = hashMap[color]
      let loc = binarySearch(map, idx)
      if (loc == 0) {
        ans.push(map[0]-idx)
      } else if (loc == map.length) {
        ans.push(idx-map[map.length-1])
      } else {
        ans.push(Math.min(idx-map[loc-1], map[loc]-idx))
      }
    }
  }
  return ans
};

console.log(shortestDistanceColor([1,1,2,1,3,2,2,3,3], [[1,3],[2,2],[6,1]]))