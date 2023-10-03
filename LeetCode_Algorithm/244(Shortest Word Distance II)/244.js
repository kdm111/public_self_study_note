var WordDistance = function(wordsDict) {
  // O(n) 131ms 78ms
  this.hashMap = new Map()    
  for (let [idx, word] of wordsDict.entries()) {
    if (this.hashMap[word] == undefined) {
      this.hashMap[word] = [idx]
    } else {
      this.hashMap[word].push(idx)
    }
  }
};

WordDistance.prototype.shortest = function(word1, word2) {
  ans = Infinity
  let idx1 = 0; let idx2 = 0;
  while (idx1 < this.hashMap[word1].length && idx2 < this.hashMap[word2].length) {
    ans = Math.min(ans, Math.abs(this.hashMap[word1][idx1]-this.hashMap[word2][idx2]))
    if (this.hashMap[word1][idx1] < this.hashMap[word2][idx2]) {
      idx1++
    } else {
      idx2++
    }
  } 
  return ans
};