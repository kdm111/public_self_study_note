var minEatingSpeed = function(piles, h) {
  // sol1 64ms 97% 45.8MB 22%
  let l = 1; let r = Math.max(...piles)
  while (l < r) {
    let m = Math.floor((l + r) / 2)
    let hours = solve(piles, m)
    if (hours > h)
      l = m + 1
    else 
      r = m
  }
  return l
};

var solve = (piles, m) => {
  let ret = 0
  for (let pile of piles) {
    ret += Math.ceil(pile / m)
  }
  return ret
}

console.log(minEatingSpeed([3,6,7,11], 8))