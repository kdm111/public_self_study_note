var repeatedCharacter = function(s) {
  // sol1 62ms 79% 42.2MB 32%
  let check = new Set()
  for (let c of s) {
    if (check.has(c)) {
      return c
    }
    check.add(c)
  }  
};