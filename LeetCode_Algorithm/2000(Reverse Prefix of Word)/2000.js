var reversePrefix = function(word, ch) {
  // sol1 55ms 95% 42MB 47%
  let idx = word.indexOf(ch)
  if (idx >= 0) {
    return word.slice(0, idx+1).split("").reverse().join("") + word.slice(idx+1, )
  } else {
    return word
  }
};

console.log(reversePrefix("abcd", 'c'))