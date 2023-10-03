isCapital = (letter) => {
  return (letter >= 'A') && (letter <= 'Z')
}
var detectCapitalUse = function(word) {
  // sol1  80ms 65% 42.2MB 60%
  if (word.length == 1)
    return true
  if (!isCapital(word[0]) && isCapital(word[1]))
    return false
  capital = isCapital(word[1])
  for (let i=2; i < word.length; i++) {
    if (capital != isCapital(word[2]))
      return false
  }
  return true
};
console.log(detectCapitalUse("Leet"))
console.log(detectCapitalUse("lEet"))