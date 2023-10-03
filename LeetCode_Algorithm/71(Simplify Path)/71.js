var simplifyPath = function(path) {
  // sol2 80ms 36% 44.6MB 20%
  let i = 0
  stack = []
  while (i < path.length) {
    temp = ""
    while (i < path.length && path[i] != '/') {
      temp += path[i]
      i += 1
    }
    if (temp != "") {
      stack.push(temp)
    }
    i += 1
  }
  part = []
  for (let st of stack) {
    if (st == "..") {
      if (part) {
        part.pop()
      }
    }
    else if (st == '.') {
      continue
    }
    else {
      part.push(st)
    }
  }  
  if (part.length == 0) {
    return '/'
  }
  let ans = ""
  for (let st of part) {
    ans += '/' + st
  }
  return ans
};