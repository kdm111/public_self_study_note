var topKFrequent = function(words, k) {
 // 165ms 11?%
  const hashMap = {}
  for (let word of words) {
    hashMap[word] = hashMap[word]+1|| 1
  }

  ans = Object.keys(hashMap).sort((a,b) =>{

    if (hashMap[b] - hashMap[a] == 0) {
      return a.localeCompare(b)
    }
    return hashMap[b]-hashMap[a]
  })
  return ans.slice(0, k)
};
// console.log(topKFrequent(["the","day","is","sunny","the","the","the","sunny","is","is"], 4))
console.log(topKFrequent(["i","love","leetcode","i","love","coding"], 3))
