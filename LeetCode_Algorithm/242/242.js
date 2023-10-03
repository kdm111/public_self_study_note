var isAnagram = function(s, t) {
  // sol1 O(nlogn), O(n) 96~124ms 75~43%
  // if (s.length != t.length) { return false }
  // sArray = s.toLowerCase().split("").sort()
  // tArray = t.toLowerCase().split("").sort()

  // for (let i=0; i < sArray.length; i++){
  //   if (sArray[i] != tArray[i]) { return false }
  // }
  // return true

  // sol2 O(n), O(n) 94~116ms 76~54%
  if (s.length != t.length) { return false }
  sHashMap = {}
  tHashMap = {}

  for (let c of s){
    if (sHashMap[c] == undefined) {
      sHashMap[c] = 1
    }else{
      sHashMap[c] += 1
    }
  }

  for (let c of t){
    if (tHashMap[c] == undefined){
      tHashMap[c] = 1
    }else{
      tHashMap[c] += 1
    }
  }

  for (let k in sHashMap){
    if (sHashMap[k] != tHashMap[k]) { return false }
  }
  return true


};

console.log(isAnagram("cbt", "cat"))