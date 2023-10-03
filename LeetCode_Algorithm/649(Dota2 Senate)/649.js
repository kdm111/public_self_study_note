var predictPartyVictory = function(senate) {
  // sol1 77ms 67% 45MB 71%
  let rQueue = []; let qQueue = []
  for (let i = 0; i < senate.length; i++) {
    if (senate[i] == 'R') {
      rQueue.push(i)
    } else {
      qQueue.push(i)
    }
  }
  while (rQueue.length && qQueue.length) {
    let r= rQueue.shift()
    let q = qQueue.shift()
    if (r < q) {
      rQueue.push(r + senate.length)
    } else {
      qQueue.push(q+senate.length)
    }
  }
  return rQueue.length != 0 ? "Radiant" : "Dire"
};