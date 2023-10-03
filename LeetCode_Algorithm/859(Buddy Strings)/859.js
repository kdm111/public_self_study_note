var buddyStrings = function(s, goal) {
  // sol1 100ms 62% 44.1MB 39%
  if (s.length != goal.length) 
    return false
  if (s == goal) {
    return new Set(s).size < s.length
  }
  let diff = []
  for (let i=0; i < s.length; i++) {
    if (s[i] != goal[i])
      diff.push([s[i], goal[i]])
    if (diff.length > 2)  
      return false
  }
  if (diff.length == 2) {
    let rev = diff[1].reverse()
    return diff.length == 2 && arrCheck(diff[0], rev)
  }
  return false
};
var arrCheck = (arr1, arr2) => {
  for (let i=0; i < arr1.length; i++) {
    if (arr1[i] != arr2[i])
      return false
  } 
  return true
}

console.log(buddyStrings("ab", "ba"))