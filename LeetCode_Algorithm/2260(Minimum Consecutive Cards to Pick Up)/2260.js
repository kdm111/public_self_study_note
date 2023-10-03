var minimumCardPickup = function(cards) {
  // sol1 539ms 12% 94MB 17%
  let cnt = new Map()
  for (let i=0; i < cards.length; i++) {
    if (cnt[cards[i]] == undefined) {
      cnt[cards[i]] = [i]
    } else {
      cnt[cards[i]].push(i)
    }
  }
  ans = Infinity
  for (let k in cnt) {
      for (let i=0; i < cnt[k].length-1; i++) {
          ans = Math.min(ans, cnt[k][i+1]-cnt[k][i]+1)
      }
  }
  if (ans == Infinity) {
      return -1
  }
  return ans
};