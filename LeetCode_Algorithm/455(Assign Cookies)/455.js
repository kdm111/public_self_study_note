var findContentChildren = function(g, s) {
  // sol1 111ms 56% 44.2MB 91%
    g.sort((a,b) => {return a-b})
    s.sort((a,b) => {return a-b})
    let gIdx = 0; let sIdx = 0; let ans = 0
    while (gIdx < g.length && sIdx < s.length) {
      if (g[gIdx] <= s[sIdx]) {
        gIdx += 1; ans += 1
      }
      sIdx += 1
    }
    return ans
};