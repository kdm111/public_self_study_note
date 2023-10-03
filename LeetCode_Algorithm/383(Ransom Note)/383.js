var makeMap = function(note) {
  // 181ms 13%
  let hashMap = new Map();
  for (let char of note) {
    if (hashMap[char] == undefined) {
      hashMap[char] = 1
    } else {
      hashMap[char] += 1
    }
  }
  return hashMap
}
var canConstruct = function(ransomNote, magazine) {
  let ransomNoteMap = makeMap(ransomNote)
  let magazineMap = makeMap(magazine)
  for (let key in ransomNoteMap) {
    if (magazineMap[key] < ransomNoteMap[key]) {
      return false
    } else if (magazineMap[key] == undefined) {
      return false
    }
  }
  return true
};

console.log(canConstruct("aa", "ab"))