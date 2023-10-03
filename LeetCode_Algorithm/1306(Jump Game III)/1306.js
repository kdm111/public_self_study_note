var canReach = function(arr, start) {
  // sol1 66ms 93% 47MB 82%
  let queue = [start]
  while (queue.length) {
    let node = queue.shift()
    if (arr[node] == 0)
      return true
    if (arr[node] > 0) {
      for (let n of [node + arr[node], node - arr[node]]) {
        if (0 <= n && n < arr.length)
          queue.push(n)
      }
    }
    arr[node] = -1
  }  
  return false
};