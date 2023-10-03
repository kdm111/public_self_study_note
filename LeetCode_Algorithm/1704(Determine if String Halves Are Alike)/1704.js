var halvesAreAlike = function(s) {
  // 113ms 34% 43.2MB 53%
  let firstHalf = 0; let secondHalf = 0;
  const vowels = {
    'a' : 1, 'e' : 1, 'i' : 1, 'o' : 1, 'u' : 1,
    'A' : 1, 'E' : 1, 'I' : 1, 'O' : 1, 'U' : 1
  }
  for (let i=0; i < s.length; i++) {
    if (i >= s.length/2) {
      firstHalf += (vowels[s[i]] != undefined)
    } else {
      secondHalf += (vowels[s[i]] != undefined)
    }
  }
  return firstHalf == secondHalf
};