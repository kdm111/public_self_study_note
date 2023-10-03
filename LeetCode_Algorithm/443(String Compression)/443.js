var compress = function(chars) {
  // 79ms 45% 45.1MB 14%
  let j = 0; let temp = []
  while (j < chars.length) {
    let i = j; let string = ""
    while (j < chars.length && chars[i] == chars[j]) {
      string += chars[j]
      j += 1
    }
    temp.push(string)
  }
  while (chars.length)
    chars.pop()
  for (let string of temp) {
    chars.push(string[0])
    if (string.length != 1) {
      let lenString = String(string.length)
      for (let c of lenString) {
        chars.push(c)
      }
    }
  }
  return chars.length
};