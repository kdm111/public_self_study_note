var checkIfPangram = function(sentence) {
  // sol1 126ms 12% 45.3MB 6%
  // let alpha = Array.from(Array(26)).map((_,i) => i+97)
  // let cnt = alpha.map((c) => String.fromCharCode(c))

  // for (let c of sentence) {
  //   if (cnt.indexOf(c) >= 0) {
  //     cnt.splice(cnt.indexOf(c), 1)
  //   }
  // }
  // return cnt.length == 0


  // sol2 119ms 12% 44MB 19%
  // let cnt = new Map()
  // for (let i=97 ; i < 123; i++) {
  //   cnt[String.fromCharCode(i)] = 0
  // }
  // for (let c of sentence) {
  //   cnt[c] += 1
  // }
  // for (const [k,v] of Object.entries(cnt)) {
  //   if (v == 0) {
  //     return false
  //   }
  // }
  // return true

  // sol3 70ms 88% 43.5MB 38%
  let seen = new Set(sentence)
  return seen.size == 26
  
};

console.log(checkIfPangram("abca"))