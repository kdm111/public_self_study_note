var minSpeedOnTime = function(dist, hour) {
  // sol1 153ms 70% 54.2MB 20%
  if (dist.length - 1 >= hour)
    return -1
  let l = 1; let r = 10 ** 7
  while (l < r) {
    let m = Math.floor((l + r) / 2)
    if (solve(dist, m) <= hour)
      r = m - 1
    else
      l = m + 1
  }
  return l
};

var solve = (dist, m) => {
  let ret = 0
  for (let d of dist) {
    ret = Math.ceil(ret)
    ret += d / m
  }
  return ret
}

console.log(minSpeedOnTime([1,1], 1.0))
console.log(minSpeedOnTime([1,3,2], 2.7))
