var removeDuplicates = function(s, k) {
  // sol1 89ms 93% 53.5MB 29%

  let stack = []; let cntArr = []
  for (let c of s) {
    if (stack.length && cntArr[cntArr.length-1][0] == c) {
      cntArr[cntArr.length-1][1] += 1
      stack.push(c)
      if (cntArr[cntArr.length-1][1] == k) {
        while (cntArr[cntArr.length-1][1]) {
          cntArr[cntArr.length-1][1] -= 1
          stack.pop()
        }
        cntArr.pop()
      }
    } else {
      stack.push(c)
      cntArr.push([c, 1])
    }
  }
  return stack.join("")
};