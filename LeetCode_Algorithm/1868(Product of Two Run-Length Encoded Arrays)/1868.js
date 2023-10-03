var findRLEArray = function(encoded1, encoded2) {
  // sol2 824ms 71%
  let idx1 = 0; let idx2 = 0;
  let ans = []
  while (idx1 < encoded1.length && idx2 < encoded2.length) {
    let val = encoded1[idx1][0] * encoded2[idx2][0]
    let cnt = Math.min(encoded1[idx1][1], encoded2[idx2][1])
    encoded1[idx1][1] -= cnt; encoded2[idx2][1] -= cnt
    if (ans.length > 0 && ans[ans.length-1][0] == val) {
      ans[ans.length-1][1] += cnt
    } else {
      ans.push([val, cnt])
    }
    if (encoded1[idx1][1] == 0) {
      idx1 += 1
    }
    if (encoded2[idx2][1] == 0) {
      idx2 += 1
    }
  }
  return ans
};