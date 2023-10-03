var mergeAlternately = function(word1, word2) {
  // sol2 51ms 91% 42.5MB 35%
  // if (word1.length && word2.length)
  //   return word1[0] + word2[0] + mergeAlternately(word1.slice(1, ), word2.slice(1, ))
  // return word1.length ? word1 : word2


  // sol3 39ms 99% 42.6MB 29%
  // let i = 0; let ans = []
  // let word1Len = word1.length; let word2Len = word2.length
  // while (i < word1Len || i < word2Len) {
  //   if (i < word1Len)
  //     ans.push(word1[i])
  //   if (i < word2Len)
  //     ans.push(word2[i])
  //   i += 1
  // }
  // return ans.join("")

  // sol3 61ms 45% 42.4MB 50%
  let i = 0; let ans = []
  let word1Len = word1.length; let word2Len = word2.length
  while (i < word1Len && i < word2Len) {
    ans.push(word1[i])
    ans.push(word2[i])
    i += 1
  }
  if (i < word1Len)
    ans.push(...word1.slice(i, ))
  else
    ans.push(...word2.slice(i, ))
  return ans.join("")
};
