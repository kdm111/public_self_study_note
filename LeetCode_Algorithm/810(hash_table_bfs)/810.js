var numBusesToDestination = function(routes, source, target) {
  // sol1 961ms 23%
  var station_bus = {}
  for (let [bus, route] of routes.entries()) {
    for (let station of route) {
      if (station_bus[station] == undefined) {
        station_bus[station] = [bus]
      } else {
        station_bus[station].push(bus)
      }
    }
  }

  let queue = [[source, 0]]
  let visited_bus = new Set()
  while (queue.length) {
    let temp = queue.shift()
    // slice 사용시 시간 초과
    //temp = queue.slice()
    let station = temp[0]; let k = temp[1]
    if (station == target) {
      return k
    }
    for (let bus of station_bus[station]) {
      if (visited_bus.has(bus)) {
        continue
      }
      visited_bus.add(bus)
      for (let station of routes[bus]) {
        if (station == target) {return k+1}
        queue.push([station, k+1])
      }
    }
  }
  return -1
};

console.log(numBusesToDestination([[1,2,7],[3,6,7]],1, 6))
console.log(numBusesToDestination([[7,12],[4,5,15],[6],[15,19],[9,12,13]],15, 12))
