var groupAnagrams = function(strs) {
  // sol1 O(nklogk) 191ms 62%
  hashMap = {}
  for (let str of strs) {
    let temp = str.split("").sort().join("")
    if (hashMap[temp] == undefined) {
      hashMap[temp] = [str]
    } else{
      hashMap[temp].push(str)
    }
  }

  return [...Object.values(hashMap)]

};

console.log(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))