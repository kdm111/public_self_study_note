var canVisitAllRooms = function(rooms) {
  // sol1 69ms 66% 44.1MB 49%
  let seen = new Set([0]);
  var solve = (roomNumber) => {
    for (let canVisit of rooms[roomNumber]) {
      if (!seen.has(canVisit)) {
        seen.add(canVisit)
        solve(canVisit)
      }
    }
  }
  solve(0)
  return seen.size == rooms.length
};