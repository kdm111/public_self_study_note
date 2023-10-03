var canBeEqual = function(target, arr) {
  // sol1 82ms 77% 48.3MB 5%
  let targetMap = makeMap(target); let arrMap = makeMap(arr)

  if (target.length != arr.length || Object.keys(target).length != Object.keys(arr).length) 
    return false
  for (let key in targetMap) {
    if (!arrMap[key])
      return false
    arrMap[key] -= targetMap[key]
  }
  for (let key in arrMap) {
    if (arrMap[key] != 0) 
      return false
  }
  return true
};

var makeMap = (arr) => {
  let hashMap = {}
  for (let num of arr) {
    if (hashMap[num]) {
      hashMap[num] += 1
    } else {
      hashMap[num] = 1
    }
  }
  return hashMap
}

console.log(canBeEqual([1,2,1],[1,2,1]))