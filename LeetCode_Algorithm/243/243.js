var shortestDistance = function(wordsDict, word1, word2) {
  // sol1 O(n^2), O(1) 94~110ms 38~16%

  var ans = 999999999
  var word1Idx = -1; var word2Idx = -1;
  for (let idx=0; idx<wordsDict.length; idx++){
    if (wordsDict[idx] == word1) { word1Idx = idx }
    else if (wordsDict[idx] == word2) {word2Idx = idx}
    if (word1Idx != -1 && word2Idx != -1) {
      ans = Math.min(ans, Math.abs(word1Idx-word2Idx))
    }
  }
  return ans
};

console.log(shortestDistance(["practice", "makes", "perfect", "coding", "makes"], "coding", "practice"))