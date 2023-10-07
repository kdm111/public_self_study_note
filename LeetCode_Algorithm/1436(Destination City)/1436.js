var destCity = function(paths) {
  // sol3 55ms 62% 43.4MB 86%
  // set을 하나만 써서 두 번 반복
  // let setStarts = new Set()
  // for (let path of paths) {
  //   setStarts.add(path[0])
  // }
  // for (let path of paths) {
  //   if (!setStarts.has(path[1])) {
  //     return path[1]
  //   }
  // }

  // sol4 50ms 85% 44.5MB 33%
  // graph를 동시에 그려가면서 도착지가 'undefined'인 곳을 찾기
  let graph = new Map()
  for (let path of paths) {
    graph.set(path[0], path[1])
    graph.set(path[1], graph.get(path[1]))
  }
  for (let path of graph) {
    if (!path[1])
      return path[0]
  }
};

console.log(destCity([["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]))