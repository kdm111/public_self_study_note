var numBusesToDestination = function(routes, source, target) {
  // sol1 852ms 22%
  if (source == target) {
    return 0 ;
  }
  let hashMap = new Map()
  for (let bus in routes) {
    for (let stop of routes[bus]) {
      let key = parseInt(stop)
      if (!hashMap[key]) {
        hashMap[key] = new Set([parseInt(bus)])
      } else {
        hashMap[key].add(bus)
      }
    }
  } 

  let seenBus = new Set(); let seenStop = new Set([source])
  let queue = [[source, 0]]; let ans = Infinity
  while (queue.length > 0) {
    console.log(queue)
    let temp = queue.shift()
    let stop = temp[0]; let tempAns = temp[1]
    if (stop == target) {
      ans = Math.min(ans, tempAns)
    }
    for (let bus of hashMap[stop]) {
      if (!seenBus.has(bus)) {
        for (let stop of routes[bus]) {
          if (!seenStop.has(stop)) {
            queue.push([stop, tempAns+1])
          }
          seenStop.add(stop)
        }
      }
      seenBus.add(bus)
    }
  }
  return ans == Infinity ? -1 : ans
};

console.log(numBusesToDestination([[7,12],[4,5,15],[6],[15,19],[9,12,13]], 15, 12))