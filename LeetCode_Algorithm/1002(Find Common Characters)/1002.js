var commonChars = function(words) {
  // sol1 84ms 91%
  // 
  ans = words[0].split('')
  for (let word of words.slice(1, )) {
    temp = new Array()
    for (let c of word) {
      if (ans.indexOf(c) != -1) {
        temp.push(c)
        ans.splice(ans.indexOf(c), 1)
      }
    }
    ans = temp
  }
  return ans
};

console.log(commonChars(["bella","label","roller"]))