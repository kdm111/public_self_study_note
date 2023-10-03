var backspaceCompare = function(s, t) {
  // sol1 O(m+n), O(m+n) 63~75ms 91~68%
  // return (solve(s).join("") == solve(t).join(""))

  // sol2 O(m+n), O(1) 86~96ms 50~34%
  var sIdx = s.length-1; var tIdx = t.length-1
  while (0 <= sIdx || 0 <= tIdx) {
    let sSkip = 0; let tSkip = 0; 
    while (0 <= sIdx) {
      if (s[sIdx] == "#") {
        sSkip += 1; sIdx -= 1;
      }
      else if (0 < sSkip) {
        sSkip -= 1; sIdx -= 1;
      }
      else {
        break
      }
    }

    while (0 <= tIdx) {
      if (t[tIdx] == "#") {
        tSkip += 1; tIdx -= 1;
      }
      else if (0 < tSkip) {
        tSkip -= 1; tIdx -= 1;
      }
      else {
        break
      }
    }
    
    if (s[sIdx] != t[tIdx]) {
      return false
    }

    sIdx -= 1; tIdx -= 1
  }
  return true
};
// var solve = function(string) {
//   var arr = []
//   for (let chr of string){
//     if (chr != "#"){
//       arr.push(chr)
//     }
//     else if (0 < arr.length) {
//       arr.pop()
//     }
//   }
//   return arr
// }

console.log(backspaceCompare("nzp#o#g", "b#nzp#o#g"))