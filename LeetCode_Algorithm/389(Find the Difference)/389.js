var findTheDifference = function(s, t) {
  // sol1 70ms 93% 42.9MB 88%
  let sLetters = new Map()
  for (let c= 'a'.charCodeAt(0); c<='z'.charCodeAt(0); c++) {
    sLetters[String.fromCharCode(c)] = 0
  }
  for (let c of s) {
    sLetters[c] += 1
  }
  for (let c of t) {
    sLetters[c] -=1
    if (sLetters[c] < 0) {
      return c
    }
  }
};

console.log(findTheDifference("abc", "abcd"))