var reorderedPowerOf2 = function(n) {
  // sol1 94ms 59%
  let num = Array.from(String(n)).sort()
  num = num.join('')
  for (let i = 0 ; i < 30; i++) {
    let temp =Array.from(String(1 << i)).sort()
    temp = temp.join('')
    if (temp  === num) {
      return true
    }
  }
  return false
};
console.log(reorderedPowerOf2(46))