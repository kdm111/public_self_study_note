var openLock = function(deadends, target) {
  // sol1 369ms 67%
  let visited = new Set(deadends)
  let queue = [["0000", 0]]
  while (queue.length) {
    [num, cnt] = queue.shift()
    if (num == target) {
      return cnt
    }
    if (visited.has(num)) {
      continue
    }
    visited.add(num)
    for (let i = 0 ; i < num.length; i++) {
      let clockwise = num.substring(0,i)+turnOneWheel(num[i], 1)+num.substring(i+1, )
      let antiClockwise = num.substring(0,i)+turnOneWheel(num[i], -1)+num.substring(i+1, )
      queue.push([clockwise, cnt+1],[antiClockwise, cnt+1])
    }
  }
  return -1
};

var turnOneWheel = function(n, operand) {
  n = Number(n)
  n += operand
  if (n == 10) {
    return '0'
  } else if (n == -1) {
    return '9'
  } else {
    return String(n)
  }
}
console.log(openLock(["0201","0101","0102","1212","2002"], "0202"))

