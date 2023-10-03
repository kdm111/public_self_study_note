var arrayStringsAreEqual = function(word1, word2) {
  // sol1 180ms 5% 49.4MB 5%
  // let idx1 = 0; let idx2 = 0;
  // let str1 = 0; let str2 = 0;
  // while (idx1 < word1.length || idx2 < word2.length) {
  //   if (idx1 == word1.length || idx2 == word2.length) {
  //     return false
  //   }

  //   if (word1[idx1][str1] != word2[idx2][str2]) {
  //     return false
  //   }
  //   str1++; str2++;
  //   if (str1 == word1[idx1].length) {
  //     str1 = 0; idx1++;
  //   }
  //   if (str2 == word2[idx2].length) {
  //     str2 = 0; idx2++;
  //   }
  // }
  // return true

  // sol2 116ms 8% 43MB 6%
  // let str1 = word1.join('')
  // let str2 = word2.join('')
  // let idx = 0;
  // while (idx < str1.length && str1[idx] == str2[idx]) {
  //   idx++
  // }
  // return (str1[idx] == str2[idx])

  // sol3 95ms 29% 42MB 40%
  return word1.join('') == word2.join('')
};

console.log(arrayStringsAreEqual(["a", "b", "c"], ["ab"]))